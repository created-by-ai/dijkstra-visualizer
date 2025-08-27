# 🌟 Dijkstra Visualizer – Interactive Pathfinding Animation

> A real-time, interactive visualization of Dijkstra’s Shortest Path Algorithm using Pygame

![Dijkstra Visualizer Demo](https://img.shields.io/badge/Algorithm-Dijkstra-blue?style=for-the-badge)  
![Pygame](https://img.shields.io/badge/Python-%233776AB.svg?logo=python&logoColor=white)  
![Interactive](https://img.shields.io/badge/Interactive-Visual%20Animation-green?style=for-the-badge)

---

## 📌 Description

Dijkstra Visualizer is an interactive, real-time animation that brings Dijkstra’s shortest path algorithm to life. This tool helps you understand how Dijkstra’s algorithm explores a graph, step by step, finding the shortest path from a start node to a target node in a grid-based environment.

Perfect for students, educators, and developers learning graph algorithms, this visualizer makes abstract concepts tangible with:

- Live node exploration (blue)
- Final path reconstruction (green)
- Click-and-draw interface
- Step-by-step animation

Whether you're studying algorithms or teaching computer science, Dijkstra Visualizer makes learning intuitive and fun!

---

## 🎮 Features

✅ Real-time Animation – Watch the algorithm expand from the start node  
✅ Interactive Grid – Place start, end, and walls with mouse clicks  
✅ Color-Coded States:

- 🔴 Red = Start node
    - 🟠 Orange = Goal node
    - 🟦 Blue = Nodes being processed
    - 🟩 Green = Final shortest path
    - ⬛ Black = Obstacles (walls)  
        ✅ Keyboard Control – Press `SPACE` to start Dijkstra  
        ✅ Undo & Edit – Right-click to remove nodes or walls  
        ✅ Simple & Lightweight – Built with pure Pygame and Python

---

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.7+
- `pygame` library

### Install Dependencies

```
pip install pygame
```

### Run the Visualizer

```
python dijkstra_visualizer.py
```

> 💡 Make sure you're in the directory containing the script.

---

## 🖱️ How to Use

1. Left-click to place:
    
    - First click: Start (S)
    - Second click: End (E)
    - Other clicks: Walls (obstacles)
2. Right-click to:
    
    - Remove a node (start/end)
    - Delete a wall
3. Press SPACE to start the algorithm.
    
4. Watch the blue wave expand across the grid until it reaches the goal.
    
5. The final green path shows the shortest route.
    

---

## 🔄 Algorithm Details

- Dijkstra’s Algorithm with unit edge weights (each step costs 1).
- Uses a priority queue (min-heap) for efficiency.
- Time Complexity: O((V + E) log V) — optimized with `heapq`.
- Supports obstacles and dynamic grid editing.

> 🔄 _You can extend this to support weighted edges by modifying the `new_dist` calculation.__

---

## 📂 Project Structure

````
dijkstra-visualizer/
├── dijkstra_visualizer.py        # Main script
├── README.md                     # This file
├── LICENSE                       # MIT License
└── assets/                       # (Optional: add images/icons later)
```_
````

---

## 🧠 Why Use This?

- ✅ Teaching Tool: Ideal for classrooms and online tutorials.
- ✅ Learning Aid: Visualizing how Dijkstra works builds intuition.
- ✅ Open Source: Fully customizable and extendable.
- ✅ No External Dependencies: Only uses standard Python and Pygame.

---

## 📝 License

This project is licensed under the MIT License – see the LICENSE [blocked] file for details.

---

## 📬 Feedback & Contributions

Found a bug? Want a new feature?  
👉 Open an issue or submit a pull request!

We welcome contributions for:

- Weighted edge support
- Different grid types (hexagonal, 3D)
- A* integration
- Export path as image or JSON
- Sound effects or theme customization*

---

## 🧑‍💻 Author

> Created by — [Your Name]  
> 🌐 [GitHub Profile](https://github.com/yourusername)  
> 📧 [your.email@example.com](mailto:your.email@example.com)

---

## 🏁 Final Thoughts

Dijkstra Visualizer turns an abstract algorithm into a dynamic, engaging experience. Whether you're learning algorithms for the first time or teaching them to others, this tool provides clarity, fun, and insight — one pixel at a time.

🚀 Press SPACE. Watch the path unfold. Learn the algorithm.

---

> 🔗 GitHub Repo: [github.com/yourusername/dijkstra-visualizer](https://github.com/yourusername/dijkstra-visualizer)  
> 🎥 _Demo Video_: [Add YouTube link here when available]

---

Let me know if you'd like:

- A GitHub repository template
- A GitHub Actions CI/CD workflow
- A `requirements.txt` file
- A downloadable `.exe` version (via PyInstaller)