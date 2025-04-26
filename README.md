# MNIST Classification Assignment

This repository contains implementations and evaluation of three linear classifiers on the MNIST dataset (digits 0–9):

1. **Perceptron with Pocket (One-vs-All)**
2. **Softmax Regression**
3. **Linear Regression (Least Squares)**

---

## Project Structure

```
mmn11.ipynb    # Jupyter notebook with all model implementations, results, and evaluation
README.md      # Project overview and discussion points
requirements.txt
```

---

## Installation

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

This project is contained in a single Jupyter notebook (`mmn11.ipynb`). To run:

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook mmn11.ipynb
   ```
2. Execute each cell sequentially to:
   - Load and preprocess the MNIST data
   - Train the Perceptron (Pocket), Softmax Regression, and Linear Regression models
   - Generate confusion matrices, TPR summaries, and loss/error plots

---

## Evaluation Summary

### Perceptron (Pocket, One-vs-All)
- **Overall Accuracy:** ~90 %
- **Strengths:** Fast convergence with batch updates; pocket yields near-best separator quickly.
- **Weaknesses:** Fluctuating error curves for digits 3, 5, 8, 9; linear separability limits.

### Softmax Regression
- **Overall Accuracy:** ~92–93 %
- **Strengths:** Joint multiclass objective; convex cross-entropy loss ensures global convergence; probabilistic outputs.
- **Weaknesses:** Slower per epoch due to gradient computations; still linear decision boundaries.

### Linear Regression (Least Squares)
- **Overall Accuracy:** ~88.4 %
- **Strengths:** Instant closed-form solution; fastest training.
- **Weaknesses:** Objective mismatch; treats labels numerically; poorest classification accuracy.

---

## Evaluation

* **Accuracy:**
  * Linear Regression treats class labels as numeric targets and minimizes squared error, not classification loss. As a result, it only achieves ~88.4 % accuracy—lower than both Softmax (≈92–93 %) and PLA (~90 %).
  * Because the RSS objective \(\min_w\|Xw - Y\|^2\) penalizes all label errors equally, it cannot carve decision boundaries as effectively as cross-entropy or perceptron updates.
  * The worst TPRs occur on digits with similar shapes (e.g. 3, 5, 8, 9), mirroring patterns seen in the other models but with amplified misclassification rates.

* **Performance:**
  * Training is essentially instantaneous: a single call to `np.linalg.pinv` and one matrix multiplication produce the weight vector in one shot—no epochs or iterative updates required.
  * This makes Linear Regression the fastest of the three, ideal for quick baselines or when compute is severely constrained.

* **Practical Takeaways:**
  * Provides a rapid linear baseline to gauge how much classification-specific objectives improve performance.
  * Useful as a feature-extraction step—`X @ w_hat` can serve as continuous embeddings—even if it’s not the final classifier of choice.
  * For serious digit recognition tasks, switch to cross-entropy (Softmax) or hinge-loss (SVM) models, or add regularization (ridge/lasso) and nonlinear kernels for better accuracy.

---

## Discussion Points

1. **Model Trade-offs:** Accuracy vs. speed and objective alignment.
2. **Digit-wise Performance:** Harder digits (3, 5, 8, 9) consistently show lower TPR across models.
3. **Convergence Behavior:** Batch PLA shows oscillations; Softmax has smooth loss; Linear was one-shot.
4. **Recommendations:** For high-accuracy tasks, move to nonlinear models or add feature engineering.

---

## License

This project is released under the MIT License.
