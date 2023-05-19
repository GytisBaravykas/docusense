import argparse
from docusense.sense import SenseExtractor
import logging
import json


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='', help='The path of selected document.')
    parser.add_argument('--text', type=str, default=None, help='(optional) Text instead of a document')
    parser.add_argument('--lang', type=str, default='english', help='(optional) A language for improved features extraction.')
    parser.add_argument('--question', type=str, default='What are the questions?', help='(optional) The question to look in the document.')
    parser.add_argument('--min_length', type=int, default=50, help='(optional) Min length of generated summary.')
    parser.add_argument('--max_length', type=int, default=150, help='(optional) Max length of generated summary.')
    parser.add_argument('--max_answer_len', type=int, default=50, help='(optional) Max Length of generated answer.')
    parser.add_argument('--n_keywords', type=int, default=5, help='(optional) Number of keywords to return')
    opt = parser.parse_args()
    return opt


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    opt = parse_opt()
    extractor = SenseExtractor()
    output = extractor(**vars(opt))
    logging.info(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
