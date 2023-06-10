from CONFIG import config
import whisper
import os, glob


class Transcriber:
    def __init__(self):
        # find most recent files in a directory
        self.recordings_dir = os.path.join('speechtotext/services/recordings', '*')

        self.model = self.get_model()

    def get_model(self):
        return whisper.load_model("base")

    def get_audio_file(self):
        # get most recent wav recording in the recordings directory
        files = sorted(glob.iglob(self.recordings_dir), key=os.path.getctime, reverse=True)
        print('Audio file:', files)
        return files

    def to_text(self, filename,frequency_threshold=0.75):
        text_output = ""
        files = self.get_audio_file()
        print(files)
        latest_recording = [file for file in files if filename in file][0]
        print("latest recording:", latest_recording)
        # print(os.path.exists(latest_recording) and latest_recording not in transcribed)
        # if os.path.exists(latest_recording) and latest_recording not in transcribed:
        audio = whisper.load_audio(latest_recording)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        options = whisper.DecodingOptions(language='en', fp16=False)

        result = whisper.decode(self.model, mel, options)
        with open(config.TRANSCRIPT_FILE + filename, 'w') as f:
            print('no_speech_prob:', result.no_speech_prob)
            if result.no_speech_prob < frequency_threshold:
                print(result.text)
                # append text to transcript file
                f.write(result.text)

        return True

