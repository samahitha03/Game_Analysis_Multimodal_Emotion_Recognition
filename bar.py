import pandas as pd
import plotly.express as px

# File paths for the four streamers
file_path_streamer1 = '/Users/samahithar/Documents/Capstone2/Face extraction/Kasta_Output/Final_Output_Kastaclysm_Clip3.xlsx'
file_path_streamer2 = '/Users/samahithar/Documents/Capstone2/Face extraction/Lizz_Output/Final_Output_Lizz_Clip3.xlsx'
file_path_streamer3 = '/Users/samahithar/Documents/Capstone2/Face extraction/Marza_Output/Final_Output_Marza_Clip3.xlsx'
file_path_streamer4 = '/Users/samahithar/Documents/Capstone2/Face extraction/Sky_Output/Final_Output_SKy_Clip3.xlsx'

# Read the Excel sheets
streamer1_df = pd.read_excel(file_path_streamer1, sheet_name='Sheet1')
streamer2_df = pd.read_excel(file_path_streamer2, sheet_name='Sheet1')
streamer3_df = pd.read_excel(file_path_streamer3, sheet_name='Sheet1')
streamer4_df = pd.read_excel(file_path_streamer4, sheet_name='Sheet1')

# Function to calculate emotion percentages based on `final_emotion`
def calculate_emotion_percentages(df, streamer_name):
    emotion_counts = df['final_emotion'].value_counts(normalize=True) * 100
    percentages = emotion_counts.reset_index()
    percentages.columns = ['Emotion', 'Percentage']
    percentages['Streamer'] = streamer_name
    return percentages

# Calculate percentages for all streamers
streamer1_percentages = calculate_emotion_percentages(streamer1_df, 'Streamer1')
streamer2_percentages = calculate_emotion_percentages(streamer2_df, 'Streamer2')
streamer3_percentages = calculate_emotion_percentages(streamer3_df, 'Streamer3')
streamer4_percentages = calculate_emotion_percentages(streamer4_df, 'Streamer4')

# Combine data into a single DataFrame
combined_data = pd.concat([
    streamer1_percentages,
    streamer2_percentages,
    streamer3_percentages,
    streamer4_percentages
])

# Ensure all emotions are included for consistent plotting
emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
combined_data = combined_data.pivot(index='Emotion', columns='Streamer', values='Percentage').reindex(emotions).reset_index()

# Melt the data for stacked bar plotting
melted_data = combined_data.melt(id_vars='Emotion', var_name='Streamer', value_name='Percentage')

# Create the stacked bar chart
fig = px.bar(
    melted_data,
    x='Emotion',
    y='Percentage',
    color='Streamer',
    text='Percentage',
    title='Emotion Distribution Across Streamers',
    labels={'Percentage': 'Percentage (%)', 'Emotion': 'Emotions'},
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Update layout for better visuals
fig.update_traces(
    texttemplate='%{text:.1f}%',  # Show percentages on bars
    textposition='inside'        # Place text inside the bars
)
fig.update_layout(
    title=dict(x=0.5, font=dict(size=20)),
    xaxis=dict(title='Emotions', tickangle=-45),
    yaxis=dict(title='Percentage (%)', range=[0, 200]),
    legend=dict(title='Streamers', orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5),
    bargap=0.15,  # Adjust gap between bars
    plot_bgcolor='rgba(245, 245, 245, 0.9)'
)

# Show the plot
fig.show()
