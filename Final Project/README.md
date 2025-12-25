# ⚡ My Hero Academia RPG - Web Edition

A fully interactive web-based RPG game inspired by the My Hero Academia anime series. Battle iconic villains, level up your hero, and face the ultimate challenge against All For One!

## 🎮 Features

- **Interactive Web Interface** - Beautiful, anime-inspired design with smooth animations
- **Real-time Battle System** - Engage in strategic turn-based combat with visual feedback
- **Progressive Leveling** - Earn XP, level up, and unlock the final boss battle
- **Multiple Villains** - Face off against Tomura Shigaraki, Dabi, Himiko Toga, and more
- **Strategic Combat** - Choose between Quirk attacks, evasion tactics, and healing items
- **Boss Battle** - Challenge All For One when you reach level 10
- **Stats Tracking** - Monitor your hero's progress with level, XP, and battles won
- **Exploration System** - Visit iconic locations from the My Hero Academia universe

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone or download this repository**

2. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Open your browser and navigate to:**
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
my-hero-academia-rpg/
├── app.py                 # Flask application and game logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface with CSS and JavaScript
├── test_project.py       # Unit tests (optional)
└── README.md             # This file
```

## 🎯 How to Play

### Starting Your Journey
1. Enter your hero name on the start screen
2. Click "Begin Your Hero Journey" to start

### Exploration
- Click "Explore New Location" to discover new areas
- Each exploration leads to a villain encounter

### Battle System
Choose from three actions during combat:
- **⚡ Use Quirk** - High damage attack based on your level
- **🎯 Evade & Counter** - 20% chance to dodge and counter-attack
- **💊 Use Healing Item** - Restore 15-25 HP

### Leveling Up
- Defeat villains to earn XP (20-40 per victory)
- Level up every 100 XP
- Higher levels increase your attack damage

### Final Boss Battle
- Unlock at level 10
- Face All For One with enhanced abilities:
  - **💥 Ultimate Quirk** - Powerful attack (20-30 + level damage)
  - **🤝 Team-Up Attack** - Coordinated strike with allies
  - **💊 Use Healing Item** - Restore 20-30 HP

## 🎨 Game Mechanics

### Combat System
- **Hero Health:** Starts at 100 HP each battle
- **Villain Health:** Random between 50-100 HP
- **Damage Scaling:** Increases with hero level
- **Critical Evasion:** 20% chance on evasion attempts
- **Boss Health:** 150 + (Hero Level × 2)

### Locations
Explore iconic My Hero Academia locations:
- U.A. High School
- Kamino Ward
- Hosu City
- Musutafu City
- Kiyashi Ward

### Villains
Battle against:
- Tomura Shigaraki
- Kurogiri
- Dabi
- Himiko Toga
- Stain
- All For One (Final Boss)

## 🧪 Testing

Run the included unit tests (if using the original test file):
```bash
pytest test_project.py
```

Tests cover:
- Villain selection
- Battle mechanics
- Level calculation
- Boss battle functionality

## 🛠️ Technologies Used

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML5, CSS3, JavaScript (ES6)
- **Session Management:** Flask sessions for game state
- **Styling:** Custom CSS with gradients and animations

## 📋 Requirements

```
Flask==3.0.0
pytest==7.4.3
requests==2.31.0
```

## 🎓 Learning Outcomes

This project demonstrates:
- Flask web application development
- RESTful API design with JSON responses
- Session management for game state
- Frontend-backend integration
- Responsive web design
- Event-driven JavaScript programming

## 🔮 Future Enhancements

Potential features to add:
- [ ] Sound effects and background music
- [ ] More villains and heroes
- [ ] Special Quirk abilities system
- [ ] Multiplayer functionality
- [ ] Save/Load game feature
- [ ] Character customization
- [ ] Achievement system
- [ ] Leaderboards

## 📝 License

This project is created for educational purposes. My Hero Academia and all related characters are property of Kōhei Horikoshi and their respective copyright holders.

## 👨‍💻 Author

Created as a final project demonstrating web development skills with Python and Flask.

## 🙏 Acknowledgments

- Inspired by the My Hero Academia anime and manga series
- Built with Flask framework
- Designed with modern web standards

---

**Ready to become the greatest hero? Start your journey now! Plus Ultra! 💪⚡**
