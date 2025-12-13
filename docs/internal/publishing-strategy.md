# Publishing Strategy: Docusaurus + Substack

**Goal:** Implement the "POSSE" strategy (Publish on Own Site, Syndicate Elsewhere).
**Primary Principle:** The GitHub/Docusaurus site is the **Canonical Source**; Substack is the **Distribution Channel**.

---

## 1. The Workflow

1.  **Write in Markdown (Locally):**
    * Draft articles in VS Code within the Docusaurus project.
    * Benefit: Version control (Git), linting, and local preview.
2.  **Publish to Docusaurus:**
    * Commit and push to GitHub (`git push origin main`).
    * GitHub Actions automatically deploys the site.
3.  **Import to Substack:**
    * Copy the *rendered* text from the local browser preview (`http://localhost:3000/...`).
    * *Note:* Do not paste raw Markdown into Substack. Pasting the rendered HTML preserves formatting (bold, links, headers) much better.

---

## 2. SEO & Canonical Links (Critical)

To prevent "duplicate content" penalties from Google, you must designate the Docusaurus version as the original.

* **Action:** In the Substack post settings:
    1.  Go to **Settings** > **SEO Options**.
    2.  Find **Canonical URL**.
    3.  Paste the live URL of your Docusaurus article (e.g., `https://username.github.io/repo/docs/my-article`).
* **Result:** Google attributes authority to your personal domain, not Substack.

---

## 3. Handling Technical Incompatibilities

Substack has limited support for technical formatting. Use these workarounds:

| Feature | Docusaurus (Markdown) | Substack (Editor) | Workaround Strategy |
| :--- | :--- | :--- | :--- |
| **Code Blocks** | Syntax Highlighting + Copy Button | Plain text block | Use **[Carbon.now.sh](https://carbon.now.sh)** to create nice screenshots of code, or accept simpler formatting. |
| **Math (LaTeX)** | Renders natively | Not supported | **Screenshot** the rendered equation from Docusaurus and paste as an image in Substack. |
| **Interactive** | React components / Graphs | Static Images | Record a **GIF** of the interaction or graph and embed it in the newsletter. |

---

## 4. Cross-Linking & Growth Strategy

### The "Teaser" Method (For long tutorials)
* **On Substack:** Publish the "Why" and "What" (intro + 30%).
* **The Hook:** Add a button/link: *"Read the full documentation with interactive code snippets on my documentation site."*

### The "Subscriber" Loop
* **On Docusaurus:** Add a Call to Action (CTA) at the bottom of every technical article.
* **The Hook:** *"Did you find this useful? Subscribe to my Substack to get these tutorials in your inbox."*

---

## 5. Summary Checklist
- [ ] Write in Docusaurus (Markdown)
- [ ] Render locally (`npm start`)
- [ ] Copy *rendered* preview into Substack
- [ ] **Set the Canonical URL in Substack** (Crucial)
- [ ] Add images/screenshots for complex code or Math