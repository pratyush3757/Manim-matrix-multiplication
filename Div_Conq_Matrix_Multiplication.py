from manim import *

class MainTitle(Scene):
    def construct(self):
        text_main = Tex(r"Divide and Conquer \\ Matrix Multiplication").scale(1.75)
        self.play(Write(text_main))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        
class Slide1(Scene):
    def construct(self):
        text_naive = Text("Naive Matrix Multiplication:")
        self.play(Write(text_naive))
        self.wait(2)
        self.play(FadeOut(text_naive))
        
        mat_X = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        mat_Y = Matrix([[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
        mat_Z = Matrix([[80, 70, 60, 50], [240, 214, 188, 162], [400, 358, 316, 274], [560, 502, 444, 386]])

        text_mat_X = Text("X")
        text_mat_Y = Text("Y")
        text_mat_Z = Text("Z")

        group_mat_X = VGroup(mat_X, text_mat_X).arrange(UP).scale(0.75)
        group_mat_Y = VGroup(mat_Y, text_mat_Y).arrange(UP).scale(0.75)
        group_mat_Z = VGroup(mat_Z, text_mat_Z).arrange(DOWN)
        group_mat_Z_brackets = VGroup(mat_Z.get_brackets(), text_mat_Z)
        group_mat_Z_elements = VGroup(mat_Z.get_entries())
        (group_mat_Z_brackets + group_mat_Z_elements).scale(0.75).shift(2 * DOWN)

        text_two_mats = Tex(r"We have two matrices $X_{n \times n}\ Y_{n \times n}$")
        text_z_out = Tex(r"$Z_{ij} = \sum^{n}_{k=1} X_{ik} \times Y_{kj}$")
        group_two_mats_text = VGroup(text_two_mats,text_z_out).arrange(DOWN)
        self.play(FadeIn(group_two_mats_text))
        self.wait(2)
        self.play(group_two_mats_text.animate.shift(2 * DOWN + 4.5 * LEFT).scale(0.6))
        # self.next_section(skip_animations=True)
        self.next_section()
        
        self.play(FadeIn(group_mat_X))
        self.wait(1.5)

        group_mat_XY = VGroup(group_mat_X, group_mat_Y)
        
        self.play(group_mat_XY.animate.arrange(4 * RIGHT))
        self.wait(1.5)

        self.play(
            group_mat_XY.animate.shift(1.5 * UP), 
            group_two_mats_text.animate.shift(1 * UP)
        )
        self.wait(0.5)
        self.play(
            FadeIn(group_mat_Z_brackets),
            # group_mat_Z.animate.shift(2 * DOWN),
        )
        self.wait(0.5)

        # self.next_section(skip_animations=True)
        self.next_section()

        for i in range(4):
            mat_X_row = mat_X.get_rows()[i]
            rect_X = SurroundingRectangle(mat_X_row)
            self.play(FadeIn(rect_X))
            for j in range(4):
                mat_Y_col = mat_Y.get_columns()[j]
                mat_Z_elem = mat_Z.get_entries()[i*4 + j]
                rect_Y = SurroundingRectangle(mat_Y_col)
                rect_Z = SurroundingRectangle(mat_Z_elem)
                self.play(
                    # FadeIn(rect_X),
                    FadeIn(rect_Y),
                    FadeIn(rect_Z),
                    run_time = 0.5,
                )
                self.add(mat_Z_elem)
                self.play(
                    # FadeIn(mat_Z_elem),
                    Transform(mat_X_row.copy(), mat_Z_elem),
                    Transform(mat_Y_col.copy(), mat_Z_elem),
                    run_time = 0.5,
                )
                self.play(    
                    # FadeOut(rect_X),
                    FadeOut(rect_Y),
                    FadeOut(rect_Z),
                    run_time = 0.5,
                )
            self.play(FadeOut(rect_X))
        self.wait()
        
        
        self.next_section()
        text_time_naive = Tex(r"Time to find $Z = O(n^3)$").shift(0.3 * DOWN)
        self.play(FadeIn(text_time_naive))
        self.play(text_time_naive.animate.shift(2 * DOWN + 4.5 * LEFT).scale(0.6))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        
class Slide2(Scene):
    def construct(self):
        text_time_naive = Tex(r"Number of operations:").scale(1.75)
        self.play(Write(text_time_naive))
        self.play(text_time_naive.animate.shift(3.5 * UP))
        
        text_Z_AEBG = Tex(r"{{AE}} + {{BG}}")
        text_Z_AFBH = Tex(r"{{AF}} + {{BH}}")
        text_Z_CEDG = Tex(r"{{CE}} + {{DG}}")
        text_Z_CFDH = Tex(r"{{CF}} + {{DH}}")
        
        mat_X = Matrix([['A', 'B'], ['C', 'D']])
        mat_Y = Matrix([['E', 'F'], ['G', 'H']])
        mat_Z = MobjectMatrix([[text_Z_AEBG, text_Z_AFBH], [text_Z_CEDG, text_Z_CFDH]], h_buff = 2.7)

        text_mat_X = Text("X")
        text_mat_Y = Text("Y")
        text_mat_Z = Text("Z")

        group_mat_X = VGroup(mat_X, text_mat_X).arrange(UP).scale(0.75)
        group_mat_Y = VGroup(mat_Y, text_mat_Y).arrange(UP).scale(0.75)
        group_mat_Z = VGroup(mat_Z, text_mat_Z).arrange(UP)
        
        # self.next_section(skip_animations=True)
        self.next_section()
        
        self.play(FadeIn(group_mat_X))
        self.wait()

        group_mat_XY = VGroup(group_mat_X, group_mat_Y)
        
        self.play(group_mat_XY.animate.arrange(2 * DOWN))
        self.play(group_mat_XY.animate.shift(5 * RIGHT))
        self.play(group_mat_XY.animate.set_opacity(0.5))
        self.wait(0.5)
        
        self.play(
            FadeIn(group_mat_Z),
            group_mat_Z.animate.shift(1.5 * UP),
        )
        self.wait(0.5)

        # self.next_section(skip_animations=True)
        self.next_section()

        text_mults = Tex(r"{{8}} Multiplications").scale(0.8).shift(0.25 * DOWN + 0.25 * LEFT)
        self.play(FadeIn(text_mults), text_mults.animate.shift(1 * LEFT))
        
        self.play(
            text_mults.animate.set_color_by_tex("8", BLUE),
            text_Z_AEBG.animate.set_color_by_tex("AE", BLUE),
            text_Z_AFBH.animate.set_color_by_tex("AF", BLUE),
            text_Z_CEDG.animate.set_color_by_tex("CE", BLUE),
            text_Z_CFDH.animate.set_color_by_tex("CF", BLUE),
        )
        self.play(
            text_Z_AEBG.animate.set_color_by_tex("BG", BLUE),
            text_Z_AFBH.animate.set_color_by_tex("BH", BLUE),
            text_Z_CEDG.animate.set_color_by_tex("DG", BLUE),
            text_Z_CFDH.animate.set_color_by_tex("DH", BLUE),
        )
        self.wait()
        
        text_adds = Tex(r"{{4}} Additions").scale(0.8).shift(0.2 * DOWN + 0.75 * RIGHT)
        self.play(FadeIn(text_adds), text_adds.animate.shift(1 * RIGHT))

        self.play(
            text_adds.animate.set_color_by_tex("4", YELLOW),
            text_Z_AEBG.animate.set_color_by_tex("+", YELLOW),        
            text_Z_CEDG.animate.set_color_by_tex("+", YELLOW),
            text_Z_AFBH.animate.set_color_by_tex("+", YELLOW),
            text_Z_CFDH.animate.set_color_by_tex("+", YELLOW),
        )
        self.wait()
        
        
        text_complexity = MathTex(r"T(n) &= 8T \left( \dfrac{n}{2} \right) + c \cdot n^2 \\ &= O(n^3)").scale(0.8).shift(1.50 * DOWN)
        self.play(FadeIn(text_complexity))
        self.wait()
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

class Slide3(Scene):
    def construct(self):
        text_strassen_calc = Tex(r"In 1969 Volker Strassen designed a divide and conquer"
            r"\\ algorithm for this problem:").scale(0.75).shift(2 * UP)
        self.play(Write(text_strassen_calc))
        self.play(text_strassen_calc.animate.shift(1 * UP))
        
        text_p_list = MathTex(r"{{P1 &= A(F-H)}}\\"
            r"{{P2 &= (A+B)H}}\\"
            r"{{P3 &= (C+D)E}}\\"
            r"{{P4 &= D(G-E)}}\\"
            r"{{P5 &= (A+D)(E+H)}}\\"
            r"{{P6 &= (B-D)(G+H)}}\\"
            r"{{P7 &= (A-C)(E+F)}}").scale(0.75).shift(1 * LEFT)
        text_p_list2 = text_p_list.copy()
        
        self.play(Write(text_p_list))
        self.wait()

        self.play(text_p_list.animate.shift(3 * LEFT))
        self.play(text_p_list.animate.set_opacity(0.5))
        self.play(text_p_list.animate.set_opacity_by_tex("P5", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P4", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P2", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P6", 1))
        self.wait()

        text_Z_AEBG = Tex(r"{{AE}} + {{BG}}")
        text_Z_AFBH = Tex(r"{{AF}} + {{BH}}")
        text_Z_CEDG = Tex(r"{{CE}} + {{DG}}")
        text_Z_CFDH = Tex(r"{{CF}} + {{DH}}")
        mat_Z = MobjectMatrix([[text_Z_AEBG.copy(), text_Z_AFBH.copy()], [text_Z_CEDG.copy(), text_Z_CFDH.copy()]], h_buff = 2.7)
        text_mat_Z = Text("Z")
        group_mat_Z = VGroup(mat_Z, text_mat_Z.copy()).arrange(UP).scale(0.55)
        
        self.play(
            FadeIn(group_mat_Z),
            group_mat_Z.animate.shift(2.5 * DOWN + 2 * RIGHT),
        )
        self.play(group_mat_Z.animate.set_opacity(0.5))
        self.wait(0.5)

        text_eq_p5 = text_p_list2.get_part_by_tex("P5").set_opacity(0)
        text_eq_p4 = text_p_list2.get_part_by_tex("P4").set_opacity(0)
        text_eq_p2 = text_p_list2.get_part_by_tex("P2").set_opacity(0)
        text_eq_p6 = text_p_list2.get_part_by_tex("P6").set_opacity(0)
        text_plus = MathTex(r"{{+}}").scale(0.75)
        text_minus = MathTex(r"{{-}}").scale(0.75)
        group_p_5426 = VGroup(text_eq_p5, text_plus, text_eq_p4, text_minus, text_eq_p2, text_plus.copy(), text_eq_p6).arrange(DOWN).shift(2 * RIGHT)
        self.play(Write(group_p_5426))
        self.wait()

        self.play(
            TransformFromCopy(text_p_list.get_part_by_tex("P5"), text_eq_p5),
            TransformFromCopy(text_p_list.get_part_by_tex("P4"), text_eq_p4),
            TransformFromCopy(text_p_list.get_part_by_tex("P2"), text_eq_p2),
            TransformFromCopy(text_p_list.get_part_by_tex("P6"), text_eq_p6),
            text_eq_p5.animate.set_opacity(1),
            text_eq_p4.animate.set_opacity(1),
            text_eq_p2.animate.set_opacity(1),
            text_eq_p6.animate.set_opacity(1),
        )
        self.wait(2)

        text_p5426_LHS = MathTex(r"&P5 + P4 - P2 + P6\\").scale(0.75).shift(2 * RIGHT + 1.5 * UP)
        text_p5426_expand = MathTex(r"&= AE + AH + ED + DH\\"
            r"&+ DG - DE - AH - BH\\"
            r"&+ BG + BH - DG - DH").scale(0.75).shift(2 * RIGHT)
        text_p5426_reduce = MathTex(r"&= AE  + BG").scale(0.75).shift(2 * RIGHT)
        group_p_5426_1 = VGroup(text_p5426_expand, text_p5426_LHS)
        self.play(ReplacementTransform(group_p_5426, group_p_5426_1))
        self.wait(2)
        
        self.play(ReplacementTransform(text_p5426_expand, text_p5426_reduce))
        self.wait(2)

        self.remove(text_p5426_reduce)
        self.remove(text_p5426_LHS)
        text_p5426 = MathTex(r"P5 + P4 - P2 + P6")
        text_p12 = MathTex(r"P1 + P2")
        text_p34 = MathTex(r"P3 + P4")
        text_p1537 = MathTex(r"P1 + P5 - P3 - P7")
        mat_Z_1 = MobjectMatrix([[text_p5426.copy() , text_Z_AFBH.copy()], [text_Z_CEDG.copy(), text_Z_CFDH.copy()]], h_buff = 5.5)
        group_mat_Z_1 = VGroup(mat_Z_1, text_mat_Z.copy()).arrange(UP).set_opacity(0).shift(2.5 * DOWN + 2 * RIGHT).scale(0.65)
        self.add(group_mat_Z_1)
        self.play(ReplacementTransform(group_mat_Z, group_mat_Z_1), group_mat_Z_1.animate.set_opacity(1))
        self.wait()
        
        text_similarly = MathTex(r"Similarly:").scale(0.75).shift(2 * RIGHT + 2 * UP)
        self.play(Write(text_similarly))
        self.wait()

        self.play(group_mat_Z_1.animate.shift(2.5 * UP))
        
        self.play(text_p_list.animate.set_opacity(0.5))
        self.play(text_p_list.animate.set_opacity_by_tex("P1", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P2", 1))
        self.wait()
        
        mat_Z_2 = MobjectMatrix([[text_p5426.copy() , text_p12.copy()], [text_Z_CEDG.copy(), text_Z_CFDH.copy()]], h_buff = 5.5)
        group_mat_Z_2 = VGroup(mat_Z_2, text_mat_Z.copy()).arrange(UP).set_opacity(0).shift(2 * RIGHT).scale(0.65)
        self.add(group_mat_Z_2)
        self.play(ReplacementTransform(group_mat_Z_1, group_mat_Z_2), group_mat_Z_2.animate.set_opacity(1))
        self.wait()

        self.play(text_p_list.animate.set_opacity(0.5))
        self.play(text_p_list.animate.set_opacity_by_tex("P3", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P4", 1))
        self.wait()
        
        mat_Z_3 = MobjectMatrix([[text_p5426.copy() , text_p12.copy()], [text_p34.copy(), text_Z_CFDH.copy()]], h_buff = 5.5)
        group_mat_Z_3 = VGroup(mat_Z_3, text_mat_Z.copy()).arrange(UP).set_opacity(0).shift(2 * RIGHT).scale(0.65)
        self.add(group_mat_Z_3)
        self.play(ReplacementTransform(group_mat_Z_2, group_mat_Z_3), group_mat_Z_3.animate.set_opacity(1))
        self.wait()
        
        self.play(text_p_list.animate.set_opacity(0.5))
        self.play(text_p_list.animate.set_opacity_by_tex("P1", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P5", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P3", 1))
        self.play(text_p_list.animate.set_opacity_by_tex("P7", 1))
        self.wait()
        
        mat_Z_4 = MobjectMatrix([[text_p5426.copy() , text_p12.copy()], [text_p34.copy(), text_p1537.copy()]], h_buff = 5.5)
        group_mat_Z_4 = VGroup(mat_Z_4, text_mat_Z.copy()).arrange(UP).set_opacity(0).shift(2 * RIGHT).scale(0.65)
        self.add(group_mat_Z_4)
        self.play(ReplacementTransform(group_mat_Z_3, group_mat_Z_4), group_mat_Z_4.animate.set_opacity(1))
        self.wait()

        self.play(text_p_list.animate.set_opacity(1))
        self.wait()
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

class Slide4(Scene):
    def construct(self):
        text_slide4_title = Tex(r"Main Observation: \\").scale(0.75)
        text_slide4_subtitle = Tex(r"7 Multiplications of $\dfrac{n}{2} \times \dfrac{n}{2}$ matrices and \\"
                                       r"18 Additions").scale(0.75)
        group_slide4_title = VGroup(text_slide4_title, text_slide4_subtitle).arrange(1.5 * DOWN).shift(2.0 * UP)
        self.play(Write(group_slide4_title))
        self.play(group_slide4_title.animate.shift(1 * UP))
        
        text_strassen_complexity = MathTex(r"T(n) &= 7 \cdot T \left( \dfrac{n}{2} \right) + c \cdot n^2 \\"
                                           r"&= 7^2 \cdot T \left( \dfrac{n}{2^2} \right) \\"
                                           r"&\vdots\\"
                                           r"&= 7^k \cdot T \left( 2^k \right) \\"
                                           r"n &= 2^k \implies k = log_{2}n \\"
                                           ).scale(0.75).shift(3 * LEFT)
        text_strassen_complexity_1 = MathTex(r"T(n) &= 7^k \cdot T \left( \dfrac{2^k}{2^k} \right) \\"
                                           r"&= 7^k \cdot T \left( 1 \right) \\"
                                           r"&= 7^{log_{2}n} \\"
                                           r"&= n^{log_{2}7} \\"
                                           r"&= n^{2.81} \\"
                                           r"&= O(n^{2.81})").scale(0.75).shift(3 * RIGHT)
        self.play(Write(text_strassen_complexity))
        self.wait(3)
        self.play(Write(text_strassen_complexity_1))
        self.wait(3)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
