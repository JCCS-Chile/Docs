import { defineConfig } from "astro/config";
import react from "@astrojs/react";

const base = process.env.PUBLIC_BASE_PATH || undefined;

export default defineConfig({
  base,
  integrations: [react()],
  output: "static",
  site: "https://jccs-chile.github.io",
});
