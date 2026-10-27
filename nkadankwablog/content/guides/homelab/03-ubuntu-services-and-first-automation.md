+++
title = "Part 3 — Ubuntu Services, Local AI, and the First Automation Failures"
date = "2025-07-26T00:00:00+08:00"
recorded_period = "May 13–July 26, 2025"
weight = 4
description = "Connecting Ollama and n8n, testing webhooks and troubleshooting image downloads."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Moving from a plan to working services

Once Ubuntu had become the homelab's starting point, the next challenge was getting useful services running while learning how the pieces fitted together. That work overlapped with local-AI experiments on a separate Windows machine. The GPU-runtime settings and PowerShell prompts in this part belong to that environment.

The objective was more than reaching a working screen. When restarting the homelab work in July, I asked for explanations of the important steps so that another failure would be something to investigate, rather than another reason to start copying commands again.

## Ollama started, but n8n still could not connect

On May 29, Ollama repeatedly appeared as unhealthy, which also prevented n8n from starting when Compose required its dependency to pass a health check. One of the checks shown during troubleshooting was:

```text
nc -z localhost 11434 || exit 1
```

Changes to the health check and dependency configuration eventually led to output showing both containers started, but n8n's credential test continued returning `ECONNREFUSED`. Removing the startup obstacle had therefore moved the investigation forward without completing the connection between the applications.

The URL entered in that credential form was `http://localhost:11434`, while the shared-network configuration used `http://ollama:11434`. From inside n8n's container, `localhost` referred to that container itself, so the place a request started from mattered when choosing an address. The service-name address was proposed as the way forward, but the credential connection remained unconfirmed.

Some diagnostic attempts introduced their own errors. A container did not contain `bash`, `jq` was not recognized, and the PowerShell version being used rejected `&&`; these failures concerned the command environment and could not, on their own, explain Ollama's health status.

### The Compose settings behind the connection attempt

The Windows stack used the following settings during the attempt where both containers started. This fragment keeps the relevant fields and leaves the rest of the stack out:

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    runtime: nvidia
    healthcheck:
      disable: true
    networks:
      - n8n_ollama_network

  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    ports:
      - "5678:5678"
    environment:
      N8N_HOST: localhost
      N8N_PORT: "5678"
      N8N_PROTOCOL: http
      N8N_OLLAMA_BASE_URL: http://ollama:11434
    depends_on:
      - ollama
    networks:
      - n8n_ollama_network

volumes:
  ollama_data:

networks:
  n8n_ollama_network:
    driver: bridge
```

This is a historical troubleshooting configuration. Disabling the health check removed a startup gate; it did not demonstrate that Ollama was ready, and `depends_on` in this form did not wait for a successful model request. The GPU runtime was specific to the separate Windows setup and needs a compatible GPU and driver. The `latest` tags identify what the file requested at the time, not reproducible version pins.

The credential request was still reaching loopback:

```text
connect ECONNREFUSED ::1:11434
```

`::1` is IPv6 loopback. Inside n8n, that means n8n's own container. The configured environment value and the URL stored in a node's credentials are separate things to inspect; setting one does not prove that the other changed.

### Testing the host API separately

The Windows-side request was:

```powershell
curl http://localhost:11434/api/tags
```

The relevant response fields were:

```text
StatusCode        : 200
StatusDescription : OK
Content           : {"models":[]}
```

The API answered, but the model list was empty. That established HTTP access from Windows without establishing a model was installed or n8n could reach the same API.

For a repeat test, this additional command would exercise the container-to-container path using a tool available in the n8n image:

```bash
docker exec n8n wget -qO- http://ollama:11434/api/tags
```

If `wget` is missing, that is a missing diagnostic tool, not a failed Ollama response. A successful model-list request would still need to be followed by a generation test using an installed model.

## Telegram exposed a different limitation

That evening, the Telegram Trigger failed with a more specific requirement:

```text
Bad Request: bad webhook: An HTTPS URL must be provided for webhook
```

The first alternative was to try polling, but the interval and advanced controls described in the instructions were missing from the interface. An HTTP Request workflow was then attempted and returned repeated Telegram `404 Not Found` responses, leaving the task unfinished. The errors identified n8n **1.94.1** and HTTP Request node version **1**, which helps explain why advice aimed at a different interface needed checking before it could be followed.

## Connecting a Python model required an actual response test

On July 1, the local-AI work reached Python integration. Early attempts ran into missing `pip` and Python statements being entered directly at the Windows command prompt, where `from` and `model_id` were treated as commands. After entering Python 3.13.5, importing `LiteLLMModel` and constructing an object appeared to work, but that still left the question of whether it could generate a response.

The next explicit test answered that question with an API mismatch:

```text
response = model.chat("Hello! Can you tell me a fun fact?")
AttributeError: 'LiteLLMModel' object has no attribute 'chat'
```

The installed object did not expose the method suggested in the example. The follow-up generation test remained unfinished, so creating the model object was the completed step; inference through that integration was still unresolved.

## Docker Hub remained unreachable during the rebuild

By July 26, I had returned to the Ubuntu homelab with Nextcloud among the services being considered. Even the basic Docker test failed before application setup could begin:

```text
docker run hello-world
Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection
(Client.Timeout exceeded while awaiting headers)
```

An attempted remedy still produced `context deadline exceeded`, while a test against another registry worked:

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/pause
```

That difference was useful because it showed that image downloads were not failing everywhere. The Docker Hub request continued timing out even after the alternative registry pull succeeded and `jq . /etc/docker/daemon.json` appeared valid. Earlier the same day, Brave download URLs also timed out while Ubuntu mirror entries appeared in the package-update output, reinforcing the need to test each destination instead of treating connectivity as a single yes-or-no condition.

## What changed in my troubleshooting approach

These attempts exposed several different meanings of “working.” A container could start without its health check passing, an application could be running without another container reaching it, and a model object could be created without producing a response. Each needed its own test before moving on to the larger workflow.

The next phase expanded that workflow with Baserow and other services, bringing the addressing and integration problems into sharper focus in [Part 4]({{< relref "/guides/homelab/04-automation-stack-and-integrations.md" >}}).

## Separating container state from application readiness

A running container only confirms that its main process has not exited. It does not prove that the application has finished starting, that its dependencies are reachable, or that a model is available. These additional checks would separate those conditions:

```bash
docker inspect --format '{{.State.Status}} exit={{.State.ExitCode}} restarts={{.RestartCount}}' n8n
docker inspect --format '{{json .State.Health}}' n8n
docker logs --since 10m --tail 100 n8n
```

A `null` health field means that Docker has no health-check result for that container; it is not a passing result. An increasing restart count points to repeated process failures, while a stable running state with connection errors calls for checking the destination address, port and application logs. The Ollama tags response also needs to contain an installed model before a generation request can test the complete path.

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
Error code



404



Full message



{ "ok": false, "error_code": 404, "description": "Not Found" }

 Other info

Item Index



0



Node type



n8n-nodes-base.httpRequest



Node version



1 (Latest version: 4.2)



n8n version



1.94.1 (Self Hosted)



Time



29/05/2025, 20:46:04



Stack trace
```

```text
did option 1
docker pull hello-world
docker run hello-world
Using default tag: latest
Error response from daemon: Get "https://registry-1.docker.io/v2/": context deadline exceeded
Unable to find image 'hello-world:latest' locally
docker: Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)

Run 'docker run --help' for more information
```

{{< /details >}}
