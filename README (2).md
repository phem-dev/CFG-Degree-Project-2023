
# Stratobus Mission Game 

Stratobus Mission is a space-themed game created using the Pygame library. The game challenges players to navigate through various scenes and complete missions. This README provides an overview of the game structure, its features, and how to run it.


## Table of Contents

- Description
- Authors
- Acknowledgements
- API Reference
- Requirements
- Getting Started
- Installation
- Features
- Controls
- Gallery
- How to Play
- Missions
- Roadmap
- Contributing
- License

## Description

Stratobus Mission is a space-themed game targeted for learners aged 7-12 years. The aim of the game is to navigate a high-altitude, long-endurance stratospheric airship (Thales' *Stratobus*) through virtual cosmos to complete various missions while learning about and completing curriculum-based,educational tasks linked to space, weather, maths and near-Earth objects.  The game is built using the Pygame library, which provides the foundation for rendering graphics, handling events, and managing scenes. 

The game incorporates real-time API data from sources such as NASA’s Open API Portal, providing players with realistic and engaging space-related tasks, as well as a database to store player progress, scores and questions. The front-end of the application will use PyGame to render different environments the player can interact with, as well as engaging interfaces for the various tasks and challenges in the game.
## Authors

- [Natalie Martin](https://github.com/natlmartin)
- [Kirsty McVean](https://github.com/K-1105)
- [Alice Morgan](https://github.com/aliceamorgan)
- [Perrine Hemmings](https://github.com/phem-dev)
- [Louise Berridge](https://github.com/lberr8)
- [Rea Bartlett Tandon](https://github.com/reabt)


## Acknowledgements
Image Sources:
 - Home Background - [Space and Planet Background](https://www.vectorstock.com/royalty-free-vector/space-and-planet-background-planets-surface-vector-22266279)
 - Asteroid Mission Background - [Asteroid Moon Landscape](https://www.vectorstock.com/royalty-free-vector/asteroid-moon-landscape-scene-vector-26549262)
 - Sentinel Mission Background - [Space Satellite Flat Composition](https://www.vectorstock.com/royalty-free-vector/space-satellite-flat-composition-vector-34450848)
 - Mars Mission Background - [Outer Space Background](https://www.vectorstock.com/royalty-free-vector/outer-space-background-wallpaper-vector-44032244)
- ISS Mission Background - [Satellite with Astronauts in Outer Space](https://www.vectorstock.com/royalty-free-vector/satellite-with-astronauts-in-outer-space-vector-4609096)
 - Payload Mission Background - [Spacecraft Shuttle](https://www.vectorstock.com/royalty-free-vector/spacecraft-shuttle-or-ship-interior-flat-vector-31016826)
 - Quiz Background - [Spaceship Cockpit Interior](https://www.vectorstock.com/royalty-free-vector/spaceship-cockpit-interior-space-and-planets-view-vector-27231706)
 - Final Background - [Moon Landscape](https://www.vectorstock.com/royalty-free-vector/moon-landscape-with-planet-at-sky-view-vector-45054043)

Font Sources:
 - [TypewriterText](http://www.kenney.nl)



## API Reference

### NeoWs (Near-Earth Objects) - NASA OpenAPI
#### Get Near-Earth Objects

```http
  GET /neo/rest/v1/neo/browse
```
Retrieves information about near-Earth objects.

### Sentinel Hub Process API (Sentinel Hub)
#### Process Satellite Imagery

```http
  POST /api/v1/process
```
Processes satellite imagery using the Sentinel Hub Process API.

### Mars Rover Photos (NASA OpenAPI)
#### Get Mars Rover Photos

```http
  GET /mars-photos/api/v1/rovers/{rover_name}/photos
```

Retrieves photos taken by Mars rovers.

### International Space Station Location (Open Notify API)
#### Get ISS Location

```http
  GET /iss-now.json
```
Retrieves the current location of the International Space Station.



## Requirements

- Python 3.x
- Pygame library

## Getting Started

To play the Stratobus Mission game, follow the installation instructions in the Installation section. Once the game is installed, you can launch it and start navigating through the different missions. 
## Installation

Before running the game, you need to set up the required environment and dependencies. Follow these steps to ensure everything is properly installed:

**1. Python Version:** Make sure you have Python 3.x installed on your system. You can download the latest version of Python from the official Python website.

**2. Install Pygame:** The game relies on the Pygame library. To install it, open your terminal and run the following command:
```json
   pip install pygame
```
**3. Clone the Repository:** Clone or download this repository to your local machine using your preferred method. You can use the following command if you have Git installed:

   git clone https://github.com/your-username/repository-name.git 
 
**4. Install Required Modules:**
- Install the 'datetime' module:
```json
   pip install datetime
```
- Install the 'requests' module:
```json
   pip install requests
```
- Install the 'geopy' module:
```json
   pip install geopy
```
- Install the 'googletrans' module:
```json
   pip install googletrans
```
- Install the 'aiohttp' module:
```json
   pip install aiohttp
```
- Install the 'asyncio' module:
```json
   pip install asyncio
```
- Install the 'requirements.txt' module:
```json
   pip install -r requirements.txt
```
- Install the 'math' module (*Note: The 'math' module is part of Python's standard library and doesn't require installation*).
  
**5. Run the Game:** Run the game on 'main.py'.


By following these steps, you'll ensure that the required libraries and modules are installed, and you'll be ready to enjoy the game. If you encounter any issues during installation, feel free to seek assistance or refer to the project's documentation or community support.






## Features

- **Engaging Gameplay:** Experience exciting and immersive gameplay that challenges your skills and keeps you entertained and stimulated for hours. 

- **Interactive Controls:** Intuitive controls designed for easy navigation between different missions. 

- **Stunning Visuals:** Enjoy captivating space-themed graphics and visual effects that enhance the game's atmosphere and make it visually appealing.

- **Dynamic Soundtrack:** Immerse yourself in a dynamic soundtrack that loops seamlessly, complimenting the game's mood. A mute button is featured too should you wish to mute the game. 

- **Cross-Platform Compatibility:** Play the game seamlessly on different platforms, including Windows, macOS, and Linux.

- **Open-Source:** The game is open-source, allowing aspiring developers to learn, contribute, and modify the game's code.

- **Achievements and Progression:** Try to improve your own score for different missions and improve your position on the leaderboard at the end! 





## Controls

- Use the mouse to interact with buttons and elements on the screen.
- Press the 'Exit' button located at the bottom of the screen to exit or alternatively, click the 'x' button in the window's top-right (Windows) or top-left (Mac) corner to exit the game.

## Gallery

![Welcome Page](https://i.imgur.com/p6owdTb.png)

![Menu Page](https://i.imgur.com/8XKO5ao.png)

![Asteroid Mission](https://i.imgur.com/SvhmK6k.png)

![Satellite Images](https://i.imgur.com/bxhc3l2.png)

![Capture Mars](https://i.imgur.com/GaXUx6H.png)

![Payload Mission](https://i.imgur.com/lPLlE4I.png)

![Locate ISS](https://i.imgur.com/F7jkEgZ.png)

![Quiz](https://i.imgur.com/6xoTE72.png)

![Leaderboard](https://i.imgur.com/emZ4Nbd.png)
## How to Play
    1. Launch the game by following the installation instructions.
    2. Navigate through the different missions by interacting with buttons and elements.
    3. Complete missions and challenges presented in each scene.
    4. Enjoy the engaging space-themed experience and try and improve your position on the leaderboard! 
## Missions


| Mission Name         | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| Asteroid Mission     | Round the asteroids to the nearest whole number to test your mathematical astronaut skills.  |
| Satellite Images     | Capture aerial photographs of Earth and explore what your house looks like from above.         |
| Capture Mars         | Control the Mars Rover and take photos of the Martian surface in this exciting mission.        |
| Payload Mission      | Optimise data storage by packing data packets with tetrominoes in this challenging task.      |
| Locate ISS    | Test your geography skills by locating the International Space Station as it orbits the Earth *.|
| Asteroid Dodge Mission | Navigate through space while avoiding asteroids to survive in this action-packed mission.    |
| Quiz                 | Test your space knowledge and compete on the leaderboard to prove your expertise.              |

*Please note that if "Loading" is displayed, the ISS is currently somewhere over water.
## Roadmap

Here are the features and improvements that we plan to implement in the future development of the game:

### 1. Global Leaderboard
- **Objective:** Enhance the game experience by expanding the quiz leaderboard to a global scale.
- **Details:** Currently, the leaderboard stores scores locally, limiting visibility to individual devices. We aim to implement a SQL-based solution that allows players from around the world to compete and compare their scores.

### 2. Font Enhancement
- **Objective:** Enhance readability by addressing issues with specific letters in the current typewriter font.
- **Details:** We've received feedback regarding certain letters, such as "K" and "X," being difficult to read in the current font. We plan to evaluate and implement a more legible font, ensuring that all players can comfortably engage with the game's content.

### 3. Enhanced Installation Process
- **Objective:** Make it easier for players to install the game on their devices.
- **Details:** We are exploring options such as creating executable files (EXE) and developing downloadable apps for various platforms. This will streamline the installation process and provide a more accessible gaming experience.

### 4. Mobile/Tablet Compatibility
- **Objective:** Extend the game's reach to mobile devices, including phones and tablets.
- **Details:** We plan to optimize the game's user interface and controls for touch-based devices. This will enable players to enjoy the game seamlessly on a wider range of devices, making it more accessible. 

### 5. Hardware Integration
- **Objective:** Introduce hardware integration to enhance gameplay possibilities.
- **Details:** We're considering innovative features like using a programmed Raspberry Pi as a controller, adding an extra layer of interaction and engagement. This will open up new gameplay opportunities and provide a unique experience.

### 6. Additional Game Modes
- **Objective:** Expand gameplay options by introducing new and exciting game modes.
- **Details:** We're actively brainstorming and designing new game modes that challenge players in different ways. These additional modes will bring variety and freshness to the gaming experience.

### 7. Cross-Platform Multiplayer
- **Objective:** Enable players to compete with friends across different devices.
- **Details:** We're exploring the possibility of implementing cross-platform multiplayer functionality. This will allow players to challenge their friends regardless of the devices they are using.

### 8. Accessibility Improvements
- **Objective:** Make the game more inclusive and accessible to players with varying needs.
- **Details:** We are committed to ensuring that the game can be enjoyed by a diverse audience. Our accessibility efforts will include features such as customizable color schemes, keyboard shortcuts, and screen reader compatibility. We want everyone to have an enjoyable gaming experience, regardless of their abilities.

### 9. Character Creation and Username
- **Objective:** Allow players to create their own characters and usernames for a personalized gaming experience.
- **Details:** We plan to implement a feature that lets players design their own space-themed characters or astronauts at the start of the game. This will add a personal touch to the gameplay making it more engaging and making each player's experience unique.


## Contributing

Contributions to the Stratobus Mission game are always welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. 

