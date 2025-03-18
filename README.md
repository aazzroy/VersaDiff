
# Code Comparer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

**Code Comparer** is an open-source web application that allows users to compare multiple versions of code. Built with Python, Flask, CodeMirror, and Bootstrap, this tool provides a rich, interactive, and responsive interface for viewing differences between code versions with support for multiple programming languages.

## Features

- **Multi-Version Comparison:** Compare 2 to 5 code versions with side-by-side diff views.
- **Interactive Code Editors:** Utilizes [CodeMirror](https://codemirror.net/) for a modern in-browser code editing experience with syntax highlighting.
- **Responsive Design:** Styled with [Bootstrap](https://getbootstrap.com/) for a professional and mobile-friendly UI.
- **Diff Visualization:** Uses Python’s `difflib` to generate HTML diff tables with clear, color-coded differences.
- **Extensible & Modular:** Easily extend the project with advanced diffing libraries, additional language support, and further UI/UX improvements.

## Project Structure

```
code_comparer/
├── app.py              # Flask backend application
└── templates/          # HTML templates
    ├── index.html      # Landing page to select number of versions
    ├── compare.html    # Code input page with CodeMirror editors and language selectors
    └── result.html     # Display of diff comparison results
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/code_comparer.git
   cd code_comparer
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install Flask
   ```

4. **Run the Application:**

   ```bash
   python app.py
   ```

5. **Access the Application:**

   Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Future Enhancements

- **Advanced Diffing:**
  - Integrate libraries such as [diff-match-patch](https://github.com/google/diff-match-patch) or [jsdiff](https://github.com/kpdecker/jsdiff) for more robust diff comparisons.
  - Implement non-consecutive or three-way diff views.

- **Enhanced Multi-Language Support:**
  - Improve dynamic language detection and expand support to additional programming languages.
  - Enhance the UI for language selection in each CodeMirror instance.

- **UI/UX Improvements:**
  - Add more interactive features using modern JavaScript frameworks.
  - Further refine the Bootstrap-based layout for a smoother user experience.

- **Version Control Integration:**
  - Incorporate Git functionality to compare different commits or branches directly.

- **Testing & Continuous Integration:**
  - Implement automated tests and CI workflows to improve code quality and streamline contributions.

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold these standards.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact

If you have any questions, suggestions, or issues, please open an issue on the repository or contact the project maintainers.

---

Happy coding!

---
