+++
title = "Part 9 — Further AI and Automation Integration"
date = "2026-04-02T00:00:00+08:00"
recorded_period = "February 21–April 2, 2026"
weight = 10
description = "Database startup, service addressing and local AI development tools."
technical = true
+++

*Names, host addresses and other identifying values use consistent dummy examples. Exact hardware models and capacities are omitted. Commands describe this setup at the time; suggested changes are identified in the text.*

## Returning to the automation workflow

By February 21, the content-automation idea involved selecting quotes, producing text-to-speech, combining them with video backgrounds, and publishing the result. This was the intended pipeline, but the next stack session exposed more immediate problems with getting its services to start and communicate. The full publishing workflow was not working yet.

This application work took place in a separate Windows Docker environment, shown by the PowerShell prompts under `D:\DockerProjects\n8n`. It ran alongside the Ubuntu homelab work, rather than documenting the same host configuration.

## Latest images changed the database problem

On February 23, I requested latest images while revising the stack, after which PostgreSQL became unhealthy and prevented dependent services from starting. Its log described the **18+** images' use of major-version-specific data directories, shifting the investigation from an application credential problem to database startup and storage layout.

The suggested options included returning to an older compatible PostgreSQL image or resetting the data, which had very different consequences for keeping the previous database. Later startup output showed PostgreSQL healthy and newly created volumes, but Ollama was still failing. That was a useful improvement in startup without demonstrating that the older data had been preserved or migrated.

## Fixing one dependency exposed the next

Ollama then became the startup obstacle. After its health-check behaviour was changed, Compose returned:

```text
dependency failed to start: container ollama has no healthcheck configured
```

The dependency configuration still expected health information that was no longer available in that attempt. Later, n8n did start and printed `Editor is now accessible via: http://n8n:5678`, but opening that address from Windows failed because the browser could not resolve `n8n`. Its container row showed `5678/tcp` without a host-published port in that output.

This was another example of an internal address being mistaken for a browser address. A service name can make sense to another container on the same network without being resolvable from Windows, so n8n announcing its URL was not the final access test. The telemetry `ECONNRESET` in the same log also needed to be kept separate from the editor's startup message.

## Baserow still needed a working access path

Port **3000** was already used by Open WebUI's `3000:8080` mapping, so Baserow was assigned **3122** during this attempt. The displayed Baserow mapping became `3122:3122`, with `http://localhost:3122` set as its public URL, but the browser continued to reset the connection. Choosing a free host port had not established which port the application was actually accepting inside its container.

The final diagnostic request tried the upstream from inside Caddy:

```bash
docker exec caddy wget -qO- http://baserow:8080/api/_health/
```

```text
wget: can't connect to remote host (10.81.0.9): Connection refused
```

That request narrowed the failure to the tested endpoint, but did not establish a correct alternative listening port for the running configuration. Another set of checks and configuration suggestions followed, with no successful health response or browser test afterward. Baserow access therefore remained an open issue at the end of the session.

### Inspecting startup and endpoint failures separately

The upstream request from Caddy reached a refused endpoint. These additional inspections would show the published port, container state and logs before another port change:

```bash
docker compose ps --all
docker inspect baserow --format '{{json .NetworkSettings.Ports}}'
docker logs --tail 80 baserow
docker logs --tail 80 baserow_postgres
```

Use the running container names. A display of `5678/tcp` without a host binding is different from `0.0.0.0:5678->5678/tcp`: the first does not show that Windows can connect through a published port. Likewise, `3122:3122` only works if the application actually accepts requests on container port `3122`. [Compose container and port listing](https://docs.docker.com/reference/cli/docker/compose/ps/).

PostgreSQL's change in data-directory layout was a separate failure. Before changing an image or volume, these additional inspections would identify the image and attached storage:

```bash
docker inspect baserow_postgres --format '{{.Config.Image}}'
docker inspect baserow_postgres --format '{{json .Mounts}}'
```

A new healthy database on an empty volume is not a migration. The old data needs a compatible upgrade or restore procedure; deleting volumes would remove the very evidence needed to check what was preserved.

## Considering the boundaries around an AI agent

In March, the questions moved beyond service access to the design of the automation itself. Comparing self-hosted n8n and OpenClaw with the same external model led to questions about prompt injection, credentials stored in `.env`, and the protection offered by Docker. These were design questions, and the discussion did not include an exploit test or a completed change proving that the proposed boundaries worked.

The useful distinction was between choosing tools that could support a controlled workflow and demonstrating that the workflow actually enforced those controls. The same care applied to the later local-development setup.

## Continue could not handle the project context as expected

On April 2, VS Code reported that a **79 KB file** exceeded a model-related limit. The setup used Continue, `nomic-embed-text` for embeddings, and a Qwen2.5 Coder model, while the Markdown files themselves were split into sections that referred to one another. Being able to send an isolated section would not fully answer the need to understand those connections.

Suggestions involving `@codebase` did not match what I could use in the interface. The pasted configuration listed chat, edit, apply, autocomplete, and embedding roles, including repeated model entries, while the logs contained extension-registration and API-proposal messages. Those details provided things to investigate, but did not isolate the exact cause of the file limit.

A developer guide was pasted later in the session, but there was no final retrieval test confirming that the whole repository had been indexed or that a cross-file question produced the intended result. Larger context settings and different model configurations remained suggestions until such a test could demonstrate an improvement.

### The Continue model configuration

The April configuration assigned several roles to local Ollama models. The following excerpt keeps the model identifiers and roles from that setup:

```yaml
name: Local Config
version: 1.0.0
schema: v1
models:
  - name: Llama 3.1 8B
    provider: ollama
    model: llama3.1:8b
    roles:
      - chat
      - edit
      - apply
  - name: Nomic Embed
    provider: ollama
    model: nomic-embed-text:latest
    roles:
      - embed
  - name: Llama 3.1 8B
    provider: ollama
    model: llama3.1:8b
    roles:
      - autocomplete
  - name: Qwen2.5-Coder 7B
    provider: ollama
    model: qwen2.5-coder:7b
    roles:
      - chat
      - edit
      - apply
  - name: Nomic Embed
    provider: ollama
    model: nomic-embed-text:latest
    roles:
      - embed
```

The embedding model appeared twice. That is retained here to show the configuration under investigation, rather than silently present a cleaned-up file as the one that was tested. Embeddings support retrieval; they do not increase a chat model's context limit or prove that the repository was indexed.

Additional checks from the development machine would be:

```bash
ollama --version
ollama list
ollama show qwen2.5-coder:7b
```

The model list confirms which tags are available to that Ollama instance. The remaining application test is a cross-file question whose answer needs information from two known files. Inspecting the retrieved context would then show whether the failure concerns indexing, retrieval, file limits or the model's input budget. These checks were still needed; increasing a context setting alone would not confirm that retrieval worked.

## What this phase added to the earlier lessons

The repeated failures came from different layers: a database storage layout, a missing health check, an address visible only inside Docker, an unresponsive upstream port, and a model-context limitation. Keeping those separate made the troubleshooting more useful than grouping them under “the stack does not work.”

[Part 10]({{< relref "/guides/homelab/10-troubleshooting-index-and-lessons.md" >}}) collects the symptoms, the results that were actually reached, and the follow-up checks still needed to close the gaps.

## Defining an end-to-end acceptance check

Model availability, API reachability and editor integration are separate checks. These additional host-side commands would establish which models are installed and whether the local Ollama endpoint responds:

```bash
ollama list
curl -i http://localhost:11434/api/tags
```

An HTTP `200` with an empty `models` array confirms a responding endpoint but leaves model availability unresolved. The configured model name must match an installed tag. The same address also has to be evaluated from the client that uses it: `localhost` in an editor on the host refers to the host, while `localhost` inside n8n refers to the n8n container.

The final check would submit a small request from the intended client and inspect both its response and the service logs. For editor retrieval, a separate question about a known symbol in another project file would test whether useful context reaches the model. A successful chat response alone would not establish that retrieval or autocomplete works.

{{< details summary="More command output" >}}

These excerpts include longer output from the same work. Names and identifying values have been replaced; copied terminal text may contain incomplete lines.

```text
dependency failed to start: container baserow_postgres is unhealthy
PS D:\DockerProjects\n8n> docker logs baserow_postgres
Error: in 18+, these Docker images are configured to store database data in a
       format which is compatible with "pg_ctlcluster" (specifically, using
       major-version-specific directory names).  This better reflects how
       PostgreSQL itself works, and how upgrades are to be performed.

       See also https://github.com/docker-library/postgres/pull/1259

       Counter to that, there appears to be PostgreSQL data in:
         /var/lib/postgresql/data (unused mount/volume)

       This is usually the result of upgrading the Docker image without
       upgrading the underlying database using "pg_upgrade" (which requires both
       versions).

       The suggested container configuration for 18+ is to place a single mount
       at /var/lib/postgresql which will then place PostgreSQL data in a
       subdirectory, allowing usage of "pg_upgrade --link" without mount point
       boundary issues.

       See https://github.com/docker-library/postgres/issues/37 for a (long)
       discussion around this process, and suggestions for how to do so.
```

```text
PS D:\DockerProjects\n8n> docker exec caddy wget -qO- http://baserow:8080/api/_health/
wget: can't connect to remote host (10.81.0.9): Connection refused
```

{{< /details >}}
