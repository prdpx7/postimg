from setuptools import setup

setup(name="postimg",
      version="0.2",
      description="Upload/share images with imagurl.com",
      url="http://github.com/zuck007/postimg",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      packages=["postimg"],
      scripts=["./bin/postimg"],
      keywords='imgur upload share linux script cli-tool',
      install_requires=[
          "pyperclip",
          "requests",
      ],
      zip_safe=False)

