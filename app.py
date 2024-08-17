from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  "localhost",
  9090,
  lang="es",
  translate=False,
  model="tiny",
  use_vad=False,
  save_output_recording=True,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav"  # Only used for microphone input
)

client()