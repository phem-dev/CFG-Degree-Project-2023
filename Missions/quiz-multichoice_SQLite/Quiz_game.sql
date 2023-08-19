CREATE TABLE leaderboard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    score INT
);

--select * from leaderboard;



CREATE TABLE questions (
    id INTEGER PRIMARY KEY,
    Question TEXT,
    choice1 TEXT,
    choice2 TEXT,
    choice3 TEXT,
    choice4 TEXT,
    correct_answer INTEGER
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    1,
    'Which planet is known as the "Red Planet"?',
    'Earth', 'Mars', 'Jupiter', 'Venus',
    2
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
	2,
    'What is the name of the natural satellite that orbits the Earth?',
    'Sun', 'Mars', 'Moon', 'Saturn',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    3,
    'How long does it take for the Moon to orbit the Earth?',
    '1 day', '30 days', '365 days', '27.3 days',
    4
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    4,
    'The temperature on a planet dropped from -10°C to -25°C. What was the decrease in temperature?',
    '10°C', '15°C', '25°C', '35°C',
    2
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    5,
    'If it takes light approximately 8 minutes to travel from the Sun to Earth, how long does it take for light to travel from the Sun to Jupiter (which is about 5 times further from the Sun than Earth)?',
    '8 mins', '16 mins', '35 mins', '40 mins',
    4
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    6,
    'The mass of an object on Earth is 75kg. What would be its mass on the Moon, where the gravitational pull is about 1/6th of that on Earth?',
    '12.5kg', '450kg', '75kg', '69kg',
    1
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    7,
    'If there are 8 planets in our solar system and 4 of them have rings, what fraction of the planets have rings?',
    '1/2', '4/8', '2/4', '3/4',
    1
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    8,
    'Name the 8 planets in our solar system in order from the Sun',
    'Neptune, Mars, Earth, Saturn, Venus, Jupiter, Mercury, Uranus',
    'Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune',
    'Earth, Neptune, Uranus, Saturn, Jupiter, Mars, Venus, Mercury',
    'Venus, Mercury, Saturn, Earth, Mars, Neptune, Jupiter, Uranus',
    2
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    9,
    'What is the largest planet in our solar system?',
    'Earth', 'Jupiter', 'Saturn', 'Mars',
    2
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    10,
    'Which famous spacecraft was the first to land humans on the Moon?',
    'Voyager1', 'Hubble Space Telescope', 'Apollo11',  'Mars Rover',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    11,
    'What is the name of the galaxy that contains our solar system?',
    'Milky Way', 'Andromeda', 'Starry Galaxy',  'Black Hole',
    1
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    12,
    'What do we call a group of stars that form a pattern in the night sky?',
    'Star cluster', 'Solar System', 'Constellation',  'Planetarium',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    13,
    "What do we call a space rock that burns up in the Earth's atmosphere and creates a bright streak of light?",
    'Meteorite', 'Comet', 'Meteoroid',  'Asteroid',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    14,
    'Which planet is often called the "Blue Planet" due to its appearance from space?',
    'Mars', 'Venus', 'Earth',  'Neptune',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    15,
    'What do we call the path that a planet takes around the Sun?',
    'Orbit', 'Rotation', 'Revolution',  'Circulation',
    1
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    16,
    'What causes the Moon to sine at night?',
    'Its own light', 'Reflected sunlight', 'Starlight',  'Moonlight',
    2
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    17,
    'Which space agency sent humans to the Moon for the first time?',
    'ESA', 'Roscosmos', 'ISRO',  'NASA',
    4
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    18,
    'What is the name of the outermost layer of the Earth?',
    'Crust', 'Core', 'Mantle',  'Atmosphere',
    1
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    19,
    'How do scientists control satellites in space?',
    'They use a remote control', 'They take turns living in them to control them', 'They send commands from special stations on Earth',  'They use the Moon to help',
    3
);

INSERT INTO questions (id, Question, choice1, choice2, choice3, choice4, correct_answer)
VALUES (
    20,
    'Which of these is not something that satellites are used for?',
    'Taking pictures of Earth', 'Sending text messages', 'Predicting the weather',  'Growing plants on other planets',
    4
);

