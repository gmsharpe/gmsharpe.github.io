---
sidebar_position: 1
title: Hello World
description: My first deployment test
---

# Hello, World!

If you are seeing this page, the **GitHub Actions pipeline is working correctly**. 

This site is built with [Docusaurus](https://docusaurus.io/) and served via GitHub Pages.

## Testing Syntax Highlighting

Since we configured the site for Python and Terraform, let's verify that the code blocks look correct.

### Python Test
```python
def hello_world():
    message = "Infrastructure as Code is cool"
    print(f"Status: {message}")

if __name__ == "__main__":
    hello_world()

### Terraform Test
```terraform
resource "aws_s3_bucket" "example" {
  bucket = "my-test-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
