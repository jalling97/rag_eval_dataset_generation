import argparse
import os
from deepeval.synthesizer import Synthesizer

if 'OPENAI_API_KEY' not in os.environ:
    raise Exception("You must have an OpenAI API key set to the following env variable: OPENAI_API_KEY")

# argument parser
parser = argparse.ArgumentParser(
    prog="Synthetic Dataset Generator",
    description="Uses a list of documents to generate question-answer pairs for RAG evaluations",
)
parser.add_argument('-f', '--files', nargs='+', required=True)
parser.add_argument('-c', '--count', type=int, default=1)
args = parser.parse_args()

max_goldens = args.count
files = args.files

print("Making Synthesizer...")
synthesizer = Synthesizer()

print("Generating Goldens...")
try:
    synthesizer.generate_goldens_from_docs(
        document_paths=files,
        max_goldens_per_document=max_goldens,
        include_expected_output=True
    )
except Exception as exc:
    print("There was an error generating the goldens")
    raise exc
print("Generation complete!")

print("Saving the goldens...")
synthesizer.save_as(file_type='json', directory='./synthetic_data')
print("Save complete!")

