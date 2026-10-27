+++
title = "Part 4 — Expanding the Automation Stack"
date = "2025-09-26T00:00:00+08:00"
recorded_period = "August 13–September 26, 2025; continuation on October 18 and recollections on November 24"
weight = 5
description = "Baserow, Caddy, OAuth and the different paths between services."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Adapting the tutorial to an existing setup

The next stage was to bring n8n, Ollama, Baserow, and supporting media services into the same automation workflow. The YouTube tutorial I used provided a starting installation guide, but some services were already running and another stack occupied ports that the guide expected to use. Following the same broad approach therefore required changes to the actual commands and connections.

Those changes became particularly important around Baserow. The browser, n8n, and the reverse proxy did not necessarily reach it through the same address, while the application also generated URLs of its own. Getting one of those paths working could leave another broken, which explains much of the repeated troubleshooting that followed.

## Baserow's page and its API behaved differently

On August 14, one configuration published Baserow as `85:80` while setting its public URL to `http://baserow:80`. Opening `http://localhost:85/` produced a Baserow “Site not found” page, and `/login` then returned a server error. Later the web interface worked, but n8n still could not fetch the database options, so the visible page was not a reliable test of the whole integration.

Testing from inside n8n helped separate the failures. `curl` was initially missing, but switching to `wget` produced an HTTP response; another request resolved Baserow's name successfully before being refused on port 8000. The application was not simply disappearing from the network in every test.

| Result | What it helped narrow down |
|---|---|
| `curl: not found` | The diagnostic tool was missing from the container. |
| HTTP 404 from `baserow:80/api/_health` | An HTTP server answered, but the requested path did not give the expected result. |
| Connection refused after `baserow:8000` resolved | DNS worked for that request; the tested endpoint was not accepting the connection. |
| HTTP 401 on the upload request | The application answered but did not accept the request's authentication. |
| `ECONNREFUSED ...:85` | A host-published port had also been tried against a container address. |



The credential instructions also needed to match the actual node. My form asked for a host, username, and password, while several suggestions assumed there would be an API-token field. Repeating a configuration that the interface did not support could not resolve the connection, and I pointed out that mismatch more than once.

### The URL and port mismatch in configuration

One Baserow revision combined these values. The fragment preserves the mismatch under investigation:

```yaml
services:
  baserow:
    image: baserow/baserow:latest
    ports:
      - "85:80"
    environment:
      BASEROW_PUBLIC_URL: http://baserow:85
      PUBLIC_BACKEND_URL: http://baserow:85
      DATABASE_HOST: postgres
      DATABASE_NAME: baserow
      DATABASE_USER: baserow
      DATABASE_PASSWORD: EXAMPLE_DATABASE_PASSWORD
      REDIS_HOST: redis
      REDIS_PASSWORD: EXAMPLE_REDIS_PASSWORD
```

Port `85` was published on the host; port `80` was the container side of that mapping. From another container on the same network, `baserow:85` did not automatically mean the host's published port. The public URL settings also affected addresses returned by the application, so manually correcting the first request could leave later requests pointing elsewhere.

The database dependency used this readiness check in the same revision:

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -d $$POSTGRES_DB -U $$POSTGRES_USER"]
  interval: 10s
  timeout: 5s
  retries: 5
```

The doubled dollar signs pass variable references through Compose for expansion inside the container. A passing database readiness check does not test Baserow's HTTP endpoint, authentication or generated media URLs.

### Testing from inside n8n

The attempted container request was:

```bash
docker exec -it n8n curl -v http://baserow:8000/api/user/
```

The output included:

```text
* Host baserow:8000 was resolved.
```

The request then failed to connect. The name lookup and TCP connection were different stages: resolving `baserow` did not establish that port `8000` accepted requests. Other tests returned HTTP `404` or `401`, which moved the failure further along the path because an HTTP server had answered.

These additional inspections would show the container's published ports and attached networks without guessing them from the browser URL:

```bash
docker inspect baserow --format '{{json .NetworkSettings.Ports}}'
docker inspect baserow --format '{{json .NetworkSettings.Networks}}'
docker inspect n8n --format '{{json .NetworkSettings.Networks}}'
```

Compare the network names before trying another internal URL. Keep host access, internal service access and the application's returned URLs as separate tests. [Docker inspection reference](https://docs.docker.com/reference/cli/docker/inspect/).

## A database change introduced another dead end

One attempt tried to change the backend URL directly in PostgreSQL:

```sql
UPDATE core_settings SET public_backend_url='http://baserow:80';
```

```text
ERROR: column "public_backend_url" of relation "core_settings" does not exist
```

The schema on that installation did not contain the proposed column, so the statement failed rather than updating the URL. That was a useful reason to inspect the actual database structure instead of continuing to assume the suggested setting existed. The investigation also broadened to include Redis and PostgreSQL rather than concentrating only on the Baserow page.

## Bringing Caddy into the stack

By August 17, I could describe the problem more precisely: an earlier configuration had connected to the database, but returned URLs appeared to mix `baserow:80` with `baserow:85`. Caddy was introduced while trying to make the addresses consistent, with port `3000:8080` reserved for another application.

The tests then showed why host and container results could differ. A Windows request to `http://baserow.localhost/api/` received a **308 redirect** to HTTPS, while a container could ping `baserow` even though the Windows host could not resolve that Docker service name. The same name was being tested from different places, so those results did not contradict one another.

Internal TLS and trusting Caddy's certificate were discussed as the HTTPS configuration developed, but changing URLs still left n8n reporting “Error fetching options from Baserow.” The session ended with partial connectivity and an unfinished application connection, rather than a demonstrated working workflow.

## OAuth and the tunnel brought new configuration problems

On September 21, another startup attempt stopped at YAML parsing: `name: automation-stack` had been indented beneath `driver: bridge`, producing `mapping values are not allowed in this context`. That error occurred before service connectivity could be tested and needed to be treated as a configuration problem in its own right.

Later that evening, Google rejected the OAuth callback containing `n8n.localhost`, explaining that the redirect needed an acceptable public domain. Tunnel options were explored to provide a different callback address, but the Ngrok/n8n startup script then produced `curl: not found`, invalid `sleep` arguments, and command-not-found errors.

The pattern was consistent with missing tools and script-format or line-ending trouble, although the logs did not prove every part of that explanation. Subsequent attempts reached Ngrok's configuration parser, which first required a `version` property and then rejected `authtoken` in the supplied v3 structure. There was no successful OAuth callback or final tunnel test after those errors.

## What remained unfinished

An October 18 continuation used another Baserow instance with `185:80` and `1444:443`, where PostgreSQL reported that it was not yet accepting connections. That later attempt belongs to the same broader project, but it does not establish that the August setup had been repaired in the meantime.

Across these attempts, the most useful habit was to follow a request from its actual starting point through DNS, the listening port, HTTP or HTTPS, authentication, and finally the returned data. Changing several of those together made it harder to tell which part had improved, especially when a working browser page could hide a failing API connection.

The hardware story continued alongside this work in [Part 5]({{< relref "/guides/homelab/05-hardware-failure-and-mini-pc.md" >}}), while the later stack revisit appears in [Part 9]({{< relref "/guides/homelab/09-ai-and-automation-integration.md" >}}).

## Testing the service address at each boundary

For a Compose mapping such as `85:80`, a browser on the host connects to port `85`, while another container on the same network normally connects to the service name and port `80`. A URL containing the host port can therefore work from the host and fail from n8n.

These additional inspections would check the effective configuration and network membership:

```bash
docker compose config --services
docker compose ps
docker inspect --format '{{json .NetworkSettings.Networks}}' n8n
docker inspect --format '{{json .NetworkSettings.Networks}}' baserow
docker inspect --format '{{json .NetworkSettings.Ports}}' baserow
```

The two containers need a shared network for the Compose service name to resolve through Docker's internal DNS. Successful name resolution only verifies that step. `Connection refused` then points toward the selected port or listener, while an HTTP response shows that a server answered and moves the investigation to the response status and body. These checks are proposed diagnostics, not additional results from the installation.

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
PS C:\Users\labuser> docker exec -it n8n curl -v http://baserow:8000/api/user/

* Host baserow:8000 was resolved.

* IPv6: (none)

* IPv4: 10.82.0.8

*   Trying 10.82.0.8:8000...

* connect to 10.82.0.8 port 8000 from 10.82.0.9 port 34954 failed: Connection refused

* Failed to connect to baserow port 8000 after 4 ms: Could not connect to server

* closing connection #0

curl: (7) Failed to connect to baserow port 8000 after 4 ms: Could not connect to server

PS C:\Users\labuser>
```

```text
Error code



401



Full message



401 - "{\"detail\":\"Authentication credentials were not provided.\"}"

Request
```

```text
PS C:\Users\labuser\Downloads\automation-project> docker exec -it baserow_postgres psql -U [REDACTED] -d baserow

psql (15.13)

Type "help" for help.



baserow=# UPDATE core_settings SET public_backend_url='http://baserow:80';

ERROR:  column "public_backend_url" of relation "core_settings" does not exist

LINE 1: UPDATE core_settings SET public_backend_url='http://baserow:...

                                 ^

baserow=# \q

PS C:\Users\labuser\Downloads\automation-project> UPDATE core_settings SET public_backend_url='http://baserow:80';

UPDATE : The term 'UPDATE' is not recognized as the name of a cmdlet, function, script file, or operable program.

Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

At line:1 char:1

+ UPDATE core_settings SET public_backend_url='http://baserow:80';
```

```text
i need help here

OAuth Redirect URL
Error 400: invalid_request
Request details: redirect_uri=https://n8n.localhost/rest/oauth2-credential/callback flowName=GeneralOAuthFlow
Google cloud console
Invalid redirect: Must end with a public top-level domain (such as .com or .org).
Invalid Redirect: must use a domain that is a valid Top private domain .
```

```text
PS D:\DockerProjects\n8n> docker logs -f ngrok

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': `version` property is required.

ERROR:

ERROR:  If you're upgrading from an older version of ngrok, you can run:

ERROR:

ERROR:      ngrok config upgrade

ERROR:

ERROR:  to upgrade to the new format and add the version number.

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': `version` property is required.

ERROR:

ERROR:  If you're upgrading from an older version of ngrok, you can run:

ERROR:

ERROR:      ngrok config upgrade

ERROR:

ERROR:  to upgrade to the new format and add the version number.

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': `version` property is required.

ERROR:
```

```text
PS D:\DockerProjects\n8n> docker logs -f ngrok

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': YAML parsing error: yaml: unmarshal errors:

ERROR:    line 3: field authtoken not found in type config.v3yamlConfig

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': YAML parsing error: yaml: unmarshal errors:

ERROR:    line 3: field authtoken not found in type config.v3yamlConfig

ERROR:  Error reading configuration file '/var/lib/ngrok/ngrok.yml': YAML parsing error: yaml: unmarshal errors:

ERROR:    line 3: field authtoken not found in type config.v3yamlConfig
```

{{< /details >}}
