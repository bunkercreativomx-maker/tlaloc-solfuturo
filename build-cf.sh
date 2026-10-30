#!/bin/sh
# Arma dist/ para Cloudflare Pages (sin archivos de repo/Vercel)
set -e
rm -rf dist && mkdir dist
for f in *; do case "$f" in dist|functions|vercel.json|build-cf.sh|node_modules) ;; *) cp -r "$f" dist/ ;; esac; done
printf '/assets/*\n  Cache-Control: public, max-age=604800\n' > dist/_headers
