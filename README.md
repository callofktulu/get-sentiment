# GetSentiment
A python sentiment analyzer with bag-of-words and machine learning algorithms

### Configuration instructions
### Installation instructions
  In its current version, GetSentiment can only be used when deployed as a Python-Django web application. Its dictionaries, which are also open-source, will be later added inside the source code.
### Operating instructions
  Current version of GetSentiment doesn't include a user interface. However, you can still make API (get) calls to receive individual word values. Example:
  localhost:(port)/getsentiment/example
  
  This would return the polarity of the word "example" if it exists in the dictionaries.
### A file manifest (list of files included)
### Copyright and licensing information
  Get sentiment is an open source project built by Tugrul Erturk for his PhD project. Other researchers and contributers are free to submit their ideas.
### Contact information
  You can reach me via my university e-mail tugrulerturk@correo.ugr.es
### Known bugs
  -The system gives an error when no word is found.
### Troubleshooting
### Credits and acknowledgments
### Changelog
- Initial commit with API access
