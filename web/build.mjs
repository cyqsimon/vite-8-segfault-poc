#!/usr/bin/env node

import "workbox-build"
import { build } from "vite";
import { VitePWA } from "vite-plugin-pwa";

await build();
