# Editorial Style Guide

## Citations and References

### Citation Style
Use **IEEE citation style** for all technical articles and blog posts.

**Format:**
- Inline citations use numbered references: `[1]`, `[2]`, etc.
- Citations appear in order of first mention in the text
- Full references listed at the end in numerical order

**Example inline citation:**
```markdown
As Masood noted [1], embeddings have become core infrastructure for AI systems.
```

**Example reference entry:**
```markdown
<Reference 
  number="1"
  author="A. Masood"
  title="The State of Embedding Technologies for Large Language Models"
  publication="Medium"
  year="2025"
  url="https://medium.com/@adnanmasood/..."
/>
```

**IEEE Reference Format:**
- **Journal articles:** `[1] A. Author, "Title of article," Abbrev. Journal Name, vol. X, no. Y, pp. ZZ-ZZ, Month Year.`
- **Books:** `[1] A. Author, Title of Book. City: Publisher, Year.`
- **Online sources:** `[1] A. Author, "Title," Publication, Year. [Online]. Available: URL`
- **Documentation:** `[1] Organization, "Title." [Online]. Available: URL`

### Using the Reference Component

Import at the top of your MDX file:
```jsx
import { Reference, References } from '@site/src/components/Reference';
```

Add references section at the end:
```jsx
<References>
  <Reference 
    number="1"
    author="A. Author"
    title="Article Title"
    publication="Publication Name"
    year="2025"
    url="https://..."
  />
</References>
```

## Writing Style

### Voice and Tone
- Use active voice
- Write in first person when sharing personal experience
- Keep technical explanations clear and concise
- Use code examples to illustrate concepts

### Technical Content
- Test all code examples before publishing
- Include language identifiers in code blocks
- Provide pros/cons lists for technical comparisons
- Link to official documentation when referencing frameworks or libraries

## Formatting

### Headings
- Use `##` for main sections
- Use `###` for subsections
- Keep heading hierarchy consistent

### Code Blocks
Always specify the language:
````markdown
```python
# Your code here
```
````

### Lists
- Use bullet points (`-`) for unordered lists
- Use numbered lists for sequential steps
- Keep list items parallel in structure

### Emphasis
- Use **bold** for important terms or emphasis
- Use `inline code` for function names, variables, and technical terms
- Use *italics* for publication titles or slight emphasis
