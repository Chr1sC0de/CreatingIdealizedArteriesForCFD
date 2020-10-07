import unittest
import pathlib as pt
import arterygen as ag


class TestGlyphToArtery(unittest.TestCase):

    input_file    = pt.Path(r"D:\Github\IdealBifurcations\docs\example_part.STEP")
    output_folder = pt.Path(r"D:\Github\IdealBifurcations\docs\example_openfoam_mesh")
    save_file     = pt.Path(r"D:\Github\IdealBifurcations\scripts\tests\test.glf")

    def setUp(self):
        assert self.input_file.exists(), "input file does not exist"
        assert self.output_folder.exists(), "output folder does not exist"
        # now empty the output folder


    def test_glyph_gen(self):
        ag.generate_ideal_bifurcation_glyph(
            self.input_file, self.save_file, self.output_folder
        )

        self.assertTrue(self.save_file.exists())

if __name__ == "__main__":
    unittest.main()