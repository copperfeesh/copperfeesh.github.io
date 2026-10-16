---
title: "HTTPS for a self-hosted server using Tailscale and Docker"
date: "2026-06-08"
slug: "tailscale-https-docker"
excerpt: "I have been using Tailscale to access various Docker containers and services on my UGREEN DXP 4800 Plus using plain HTTP because I didn't feel like managing reverse proxies and certificates..."
description: "How to configure HTTPS for self-hosted Docker containers on a NAS using Tailscale certificates and serve."
tags:
  - tailscale
  - docker
  - homelab
  - self-hosted
---

I have been using Tailscale to access various Docker containers and services on my UGREEN DXP 4800 Plus using plain HTTP because I didn't feel like managing reverse proxies and certificates. This is fine as I'm managing the environments and the Tailscale but more and more certain apps expect HTTPS.

With a bit of digging I discovered Tailscale certificates and serve.

In order to enable, go to the Tailscale admin console in a browser. Then choose DNS in the top menu and enable "MagicDNS" and "HTTPS Certificates". Also copy your "Tailnet DNS name" at the top of the page.

Then enable SSH on your NAS and SSH in and `su -` to a root prompt. Then enter the following command to enable the certs:

```bash
sudo tailscale cert [your-tailscale-dns].ts.net
```

You can use `tailscale serve` to enable services. For my setup, I'm running all containers off the same IP using different ports. For each service, you can enter a command like this (replacing 8000 with your specific port):

```bash
sudo tailscale serve --bg --https=8000 http://localhost:8000
```

If you make a mistake, you can clear the setup with:

```bash
sudo tailscale serve reset
```

If it works, you can access your services at `https://[your-tailscale-dns].ts.net:[your-port]`. This helps with apps and services that require HTTPS URLs.
