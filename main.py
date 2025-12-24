from pipeline.llm_context import create_llm_gen
from pipeline.video_summarizer import VideoSummarizer

def main():
    print("Summarizing video... starting the program")
    llm_gen = create_llm_gen() # pass options to select ??
    summarizer = VideoSummarizer(llm_gen)
    result = summarizer.summarize("input/videoplayback.mp4")
    print("\nVIDEO DESCRIPTION:\n")
    print(result.text)

if __name__ == "__main__":
    main()
