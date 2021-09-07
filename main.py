#!/usr/bin/env python3

import json
import os
import shutil
import subprocess as sp
from distutils.dir_util import copy_tree
from pathlib import Path

import click

THIS_DIR = Path(__file__).parent
EXAMPLE_DIR = THIS_DIR / "example_docs"


# do you want a contents

INDEPENDENT_SECTIONS = [
    "introduction",
    "contents",
    "project_structure",
    "logo"
]

EXAMPLE_DOCS_URL = "https://github.com/Ollivanders/adam/trunk/example_docs"


class DocsGeneration:
    def __init__(
            self,
            docs_dir: Path,
            filepath=None,
            filename="README",
            sections=None,
            make_copy=False,
            make_logo=False,
            example_docs=False,
            ignore_dir_in_tree=[],
    ):
        self.docs_dir = docs_dir
        self.filename = filename
        self.ignore_dir_in_tree = ignore_dir_in_tree
        if filepath:
            self.filepath = filepath / f"{self.filename}.md"
        else:
            self.filepath = docs_dir.parents[0] / f"{self.filename}.md"
        if self.filepath.exists() and make_copy == True:
            # TODO make a copy of the file
            pass

        self.filepath.touch(exist_ok=True)
        # read in directory and contents if it already exists
        # else create and establish, have a check from the user here though that this is defo wanted
        if not self.docs_dir.exists() or example_docs == True:
            # TODO check user really wants to do this
            self.init_docs_dir()

        if sections:
            self.sections = sections
        else:
            with (self.docs_dir / "sections_order.json").open() as sections_order_file:
                section_orders = json.loads(sections_order_file.read())
                if self.filename not in section_orders:
                    raise Exception(
                        f"Please add the desired sections into {self.docs_dir / 'section_order.json'} as a new key"
                    )
                self.sections = section_orders[self.filename]
        self.file_str = ""
        if make_logo == True:
            self.sections.insert(self.sections.index("introduction") + 1, "logo")

    @classmethod
    def get_file_title(cls, title_file):
        with title_file.open() as file:
            return file.readline().replace("#", "").strip()

    @classmethod
    def write_to_file(cls, file, contents):
        with file.open("w") as openedfile:
            openedfile.write(contents)

    @property
    def sections_dir(self):
        return self.docs_dir / "sections"

    @property
    def images_dir(self):
        return self.docs_dir / "images"

    def make_ascii_logo(self):
        project_title = self.get_file_title(self.sections_dir / "introduction.md")
        result = sp.run(
            ["figlet", "-t", "-k", project_title],
            check=True,
            capture_output=True,
            text=True,
        )
        logo_str = result.stdout
        self.append_to_file_str(logo_str)
        self.write_to_file(self.docs_dir / "logo.txt", logo_str)

    def init_docs_dir(self, use_example=True):
        if self.docs_dir.exists():
            shutil.rmtree(self.docs_dir)
        if use_example == True:
            sp.run(
                f"cd {str(self.docs_dir.parent)} && svn checkout {EXAMPLE_DOCS_URL}",
                check=True,
                shell=True,
            )
            os.rename(self.docs_dir.parent / "example_docs", self.docs_dir)
        # copy_tree(str(EXAMPLE_DIR), str(self.docs_dir))
        # (docs_dir / "docs" / "sections").mkdir(parents=True, exist_ok=False)
        # (docs_dir / "docs" / "images").mkdir(parents=True, exist_ok=False)

    def make_project_structure(self):
        project_structure_str = "## Project Structure\n\n"
        project_structure_str += "```"
        tree_command = "tree"
        if self.ignore_dir_in_tree:
            tree_command += " -I"
            tree_command += " '" + "|".join(self.ignore_dir_in_tree) + "'"
        result = sp.run(
            f"cd {str(self.docs_dir.parent)} && {tree_command}",
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        project_structure_str += result.stdout
        project_structure_str += "```\n"
        self.append_to_file_str(project_structure_str)
        self.write_to_file(self.docs_dir / "project_structure.md", project_structure_str)

    def make_contents(self):
        contents_string = "## Contents\n\n"

        for section in self.sections:
            if section not in INDEPENDENT_SECTIONS:
                section_file = self.sections_dir / (f"{section}.md")
                section_title = self.get_file_title(section_file)
                converted_title = section_title.lower().replace(" ", "-")
                contents_string += f"- [{section_title}](#{converted_title})\n"
        self.append_to_file_str(contents_string)
        self.write_to_file(self.docs_dir / "contents.md", contents_string)

    def append_to_file_str(self, append_string):
        self.file_str += append_string
        self.file_str += "\n"

    def generate_independent_section(self, doc_type):
        if doc_type == "introduction":
            file = self.sections_dir / "introduction.md"
            with file.open() as doc_file:
                self.append_to_file_str(doc_file.read())
        elif doc_type == "contents":
            self.make_contents()
        elif doc_type == "project_structure":
            self.make_project_structure()
        elif doc_type == "logo":
            self.make_ascii_logo()
        else:
            raise Exception("independent section does not exist")

    def make_git_todos(self):
        """#TODO converts todos into string and then writes them to the todo section"""
        pass

    def convert_internal_reference(self):
        self.file_str = self.file_str.replace("../images", f"./{self.docs_dir.stem}/images")

    def generate_file(self):
        for doc_type in self.sections:
            if doc_type in INDEPENDENT_SECTIONS:
                self.generate_independent_section(doc_type)
            else:
                file = self.sections_dir / (f"{doc_type}.md")
                if not file.exists():
                    raise Exception(f"{file} does not exist, please check")
                with file.open() as doc_file:
                    self.append_to_file_str(doc_file.read())

        self.convert_internal_reference()
        self.write_to_file(self.filepath, self.file_str)


def test():
    docs_dir = Path(os.getcwd()) / "docsTest"

    generator = DocsGeneration(docs_dir, filename="TEST", make_logo=True)
    generator.generate_file()


@ click.command()
@ click.option("--filename", default="README")
@ click.option("--docs-dir", default=Path(os.getcwd()) / "docs", type=Path)
@ click.option("--make-copy", default=False)
@ click.option("--make-logo", default=False)
@ click.option("-I", "--ignore-dir-in-tree", multiple=True)
@ click.option("--example-docs", default=False, help="regenerate example docs even if they exist")
def main(**kwargs):
    generator = DocsGeneration(**kwargs)
    generator.generate_file()


if __name__ == "__main__":
    print("Running adam's doc generation")
    main()
