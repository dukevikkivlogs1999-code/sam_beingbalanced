# Being Balanced — Static Site

Converted from WordPress to clean static HTML/CSS/JS.

## Structure
```
beingbalanced_local/
├── index.html          → Homepage
├── about-us-*.html     → About page
├── services.html       → Services
├── *.html              → All other pages
├── images/             → All images
└── assets/
    ├── css/            → Stylesheets
    ├── js/             → Scripts
    └── fonts/          → Web fonts
```

## Local Development
Just open `index.html` in your browser.

For live-reload dev server:
```bash
# Python
python -m http.server 3000

# Node
npx serve .
```
Then open http://localhost:3000

## Deploy to GitHub Pages
```bash
git init && git add . && git commit -m "static site"
git remote add origin https://github.com/YOUR/REPO.git
git push -u origin main
```
Then: GitHub → Settings → Pages → Source: main / root

## Adding New Pages
1. Copy `index.html` as a base template
2. Edit the content section
3. Update nav links in all pages to include the new page
# beingbalanced
# beingbalanced
# sam_beingbalanced
