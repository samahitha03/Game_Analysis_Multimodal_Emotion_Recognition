Project Title:
Emotion Analysis in Gaming Using Multimodal Data

Overview:
This project aims to analyze player emotions during gameplay using facial expression and audio data. By leveraging Convolutional Neural Networks (CNN) for facial recognition and Recurrent Neural Networks (RNN) for audio sentiment analysis, the goal is to provide game developers with actionable insights into player engagement and emotional responses, helping them design more immersive and personalized gaming experiences.

Objectives:
Detect and classify player emotions through facial expressions and audio analysis.
Analyze player engagement and emotional responses during specific gameplay moments.
Provide actionable insights to game developers for improving game design and enhancing player experience.
Dataset:
The project uses a custom dataset containing:

Audio: Player speech data in .wav format with labeled emotions.
Facial Expressions: Video frames from gameplay showing player reactions during emotional moments.
More than 10,000 labeled audio files from streamers Ravdees, Tess, Savee, and Crema.
Technologies Used:
Python
TensorFlow/Keras
OpenCV
Librosa (for audio processing)
Matplotlib & Seaborn (for data visualization)
PyTorch (for some model implementations)
Methodology:
1. Facial Emotion Detection:
Model: Convolutional Neural Networks (CNN) trained on facial expression datasets.
Goal: Detect emotions such as happiness, sadness, anger, and surprise from player facial expressions during key moments in the game.
2. Audio Sentiment Analysis:
Model: Recurrent Neural Networks (RNN) to process audio features (MFCC, spectrograms).
Goal: Analyze vocal tone and emotional content during gameplay to determine emotions like happiness, sadness, or frustration.
3. Multimodal Fusion:
Combine facial and audio data using a fusion model to increase emotion recognition accuracy and provide a holistic emotional analysis of the player’s state.
Key Findings:
High Engagement: Players were more engaged in emotional and narrative-driven gameplay moments.
Diverse Emotional Responses: Different players displayed varying emotional reactions, especially during key plot moments.
Disinterest in Action-Heavy Scenes: Some players showed lower engagement during combat-focused sections of the game.
Results and Visualizations:
The project provides several visualizations such as:

Emotion Over Time Graphs showing how player emotions evolve during specific gameplay clips.
Stacked Bar Charts representing the percentage distribution of emotions across multiple streamers.
Engagement Score Graphs indicating player engagement levels based on emotional intensity.
How Developers Can Use This:
Personalization: Tailor gameplay experiences based on individual emotional responses.
Narrative Design: Optimize emotional moments to keep players engaged throughout the game.
Content Creation: Design segments that resonate emotionally with the players to maintain high engagement.
Future Work:
Real-time Analysis: Incorporate real-time emotion tracking for dynamic game adaptation.
Expand Dataset: Include more diverse player demographics and game genres for more generalized findings.
Multi-modal Feedback: Implement haptic feedback or other sensory inputs based on emotional data.
