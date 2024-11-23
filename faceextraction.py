import cv2
import mediapipe as mp
import os

mp_face_detection = mp.solutions.face_detection

def extract_faces(video_path, output_dir, output_size=(128, 128), crop_region=(0.3, 0.0, 1.0, 0.3), frames_to_capture=(0, 20, 40)):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames_per_second = round(fps)

    print(f"Detected FPS: {fps} | Rounded FPS: {frames_per_second}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    last_valid_face = None  # Store the last valid face

    with mp_face_detection.FaceDetection(min_detection_confidence=0.1) as face_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Calculate the current frame within the second
            frame_within_second = (frame_count % frames_per_second)

            # Use tolerance to check if the frame matches the desired capture frames
            if any(abs(frame_within_second - f) < 0.5 for f in frames_to_capture):
                ih, iw, _ = frame.shape
                x_start, y_start, x_end, y_end = [int(coord * scale) for coord, scale in zip(crop_region, [iw, ih, iw, ih])]

                # Ensure cropping coordinates are within bounds
                x_start, y_start = max(0, x_start), max(0, y_start)
                x_end, y_end = min(iw, x_end), min(ih, y_end)

                # Crop to the specified region
                cropped_frame = frame[y_start:y_end, x_start:x_end]

                if cropped_frame.size == 0:
                    print(f"Empty cropped frame at frame {frame_count}")
                    continue

                rgb_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)
                results = face_detection.process(rgb_frame)

                if results.detections:
                    for detection in results.detections:
                        bboxC = detection.location_data.relative_bounding_box
                        x, y, w, h = int(bboxC.xmin * cropped_frame.shape[1]), int(bboxC.ymin * cropped_frame.shape[0]), int(bboxC.width * cropped_frame.shape[1]), int(bboxC.height * cropped_frame.shape[0])
                        face = cropped_frame[y:y+h, x:x+w]

                        if face.size > 0:  
                            resized_face = cv2.resize(face, output_size)
                            last_valid_face = resized_face  # Update the last valid face

                            # Calculate the minute, second, and frame within that second
                            minutes = int((frame_count / fps) // 60)
                            seconds = int((frame_count / fps) % 60)
                            frame_within_second = int(frame_count % frames_per_second)

                            face_filename = os.path.join(output_dir, f'face_{minutes}min_{seconds}sec_{frame_within_second}frame.jpg')
                            cv2.imwrite(face_filename, resized_face)
                        else:
                            print(f"No face found at frame {frame_count}")
                else:
                    # Use the last valid face if no face is found
                    if last_valid_face is not None:
                        print(f"Using last valid face for frame {frame_count}")
                        minutes = int((frame_count / fps) // 60)
                        seconds = int((frame_count / fps) % 60)
                        frame_within_second = int(frame_count % frames_per_second)

                        face_filename = os.path.join(output_dir, f'face_{minutes}min_{seconds}sec_{frame_within_second}frame.jpg')
                        cv2.imwrite(face_filename, last_valid_face)

            frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_path = '/Users/samahithar/Documents/Capstone2/Face extraction/Sky/Sky_Clip6.mp4'
    output_dir = '/Users/samahithar/Documents/Capstone2/Sky_Face/Sky_Clip6'

    # Define the crop region
    crop_region = (0.0, 0.0, 0.3, 0.4)




    extract_faces(video_path, output_dir, output_size=(128, 128), crop_region=crop_region, frames_to_capture=(0, 20, 40))
