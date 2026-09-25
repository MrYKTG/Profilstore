# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.

# route.py — serves README.md if present, else a status page

from aiohttp import web
import markdown
import os

routes = web.RouteTableDef()

_DEFAULT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bot Status</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex; align-items: center; justify-content: center;
            min-height: 100vh; margin: 0;
            background: #0a0e1a; color: #e6ecff;
        }
        .box {
            text-align: center;
            padding: 2rem 3rem;
            border: 1px solid rgba(0, 234, 255, 0.35);
            border-radius: 20px;
            background: rgba(8, 14, 30, 0.75);
            box-shadow: 0 0 40px rgba(0, 234, 255, 0.08);
        }
        h1 { font-size: 1.4rem; margin: 0 0 0.5rem; color: #00eaff; }
        p  { margin: 0.2rem 0; color: #98a3c0; font-size: 0.95rem; }
        code { color: #ffd166; }
    </style>
</head>
<body>
    <div class="box">
        <h1>✅ Bot is running</h1>
        <p>Uptime monitor target is healthy.</p>
        <p style="margin-top:1rem;font-size:0.8rem;opacity:0.6;">
            Add a <code>README.md</code> to render custom content here.
        </p>
    </div>
</body>
</html>"""


@routes.get("/", allow_head=True)
async def root_route_handler(request):
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")

    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            html = markdown.markdown(
                md_text,
                extensions=["fenced_code", "codehilite", "tables"],
            )
            html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README</title>
    <style>
        body {{ font-family: sans-serif; max-width: 900px; margin: auto;
                padding: 2rem; background: #f9f9f9; color: #333; }}
        pre {{ background: #282c34; color: #f8f8f2; padding: 1em;
               overflow-x: auto; border-radius: 8px;
               font-size: 14px; line-height: 1.5; white-space: pre; }}
        code {{ font-family: Consolas, Monaco, 'Andale Mono', monospace; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ccc; padding: 0.5rem; text-align: left; }}
        h1, h2, h3 {{ border-bottom: 1px solid #ddd; padding-bottom: 0.3em; }}
    </style>
</head>
<body>
{html}
</body>
</html>"""
            return web.Response(text=html_page, content_type="text/html")
        except Exception as e:
            print(f"[route] README render failed: {e}")

    return web.Response(text=_DEFAULT_PAGE, content_type="text/html")


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=8080)
