# Sorting Algorithms & Product Recommendation System

This project implements several classic sorting algorithms and a product-recommendation function built on top of them.  
All code is written in Python and uses type-generic comparators for flexible sorting.

## Features

### 🔢 Implemented Sorting Algorithms
All sorting functions support:
- Custom comparator functions  
- Optional descending/ascending order  

Included algorithms:
- **Selection Sort**  
- **Bubble Sort** (with early-stop optimization)  
- **Insertion Sort**  
- **Hybrid Merge Sort** (merge sort + insertion sort for small subarrays)  
- **Quicksort** (median-of-three pivot)

Core comparison helper:
- `do_comparison()` — wraps comparator logic and handles descending mode

### 🛒 Product Recommendation
**Function:** `recommend_products(products, sorted_by)`  
Uses sorting algorithms to:
1. Sort products by **relevance** (descending)  
2. Select the **top 30%**  
3. Sort that subset by a secondary rule:
   - `"price_low_to_high"`
   - `"price_high_to_low"`
   - `"rating"`

Each product is represented by the `Product` class (price, rating, relevance).

### 📄 File
- `solution.py` — full implementation :contentReference[oaicite:0]{index=0}

## Running
This file contains no interactive CLI; import functions as needed:

```python
from solution import recommend_products, hybrid_merge_sort
