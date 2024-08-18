# Matilde 🚀

Welcome to **Matilde**! This project is designed to perform comprehensive website audits, ensuring that site architecture, SEO practices, and robots.txt configurations are optimized and consistent across your web properties.

## Features ✨

- **Internal Links Audits**: Analyze internal links to ensure that all pages are properly linked, have no redirects, and that no-follow pages are isolated from followable ones. 🎉
- **Sitemaps Audits**: Verify that all important pages are included in your sitemaps, sitemaps are correctly referenced in robots.txt, and no pages listed in sitemaps are unavailable or redirecting. 🔥
- **Robots.txt Audits**: Ensure the presence and correctness of your robots.txt file, including proper sitemap references, to control how search engines crawl your site. 🌟


## Installation 💻

You can install the package via pip:

```bash
pip install matilde
```


---

## Usage 📚

Here's a quick example to get you started:

```python
from matilde import run_audits

# Example usage
website_url = "https://example.com"
passed, failed, found_pages = run_audits(website_url)

print("Passed Audits:", passed)
print("Failed Audits:", failed)
print("Found Pages:", found_pages)

```

## Running Tests 🧪

To run the tests, you can use the unittest module or pytest.

```bash
python -m unittest discover tests
# or
pytest
```

## Contributing 🤝

We welcome contributions from the community! Here’s how you can get involved:

1. **Report Bugs**: If you find a bug, please open an issue [here](https://github.com/alexruco/matilde/issues).
2. **Suggest Features**: We’d love to hear your ideas! Suggest new features by opening an issue.
3. **Submit Pull Requests**: Ready to contribute? Fork the repo, make your changes, and submit a pull request. Please ensure your code follows our coding standards and is well-documented.
4. **Improve Documentation**: Help us improve our documentation. Feel free to make edits or add new content.


### How to Submit a Pull Request

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request on the original repository.

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software in accordance with the terms outlined in the [LICENSE](LICENSE) file.




