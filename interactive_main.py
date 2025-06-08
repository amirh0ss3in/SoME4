from manim import *
import random
import itertools

class Introduction(Scene):
    def construct(self):
        # --- CONFIGURATION (unchanged) ---
        node_radius = 0.3
        PLUS_ONE_COLOR = BLUE_D
        MINUS_ONE_COLOR = RED_D
        TEXT_COLOR = YELLOW
        J_COLOR = YELLOW
        H_COLOR = GREEN
        # --- TITLE TEXT (unchanged) ---
        title = MarkupText(f'Each person decides <span color="{YELLOW}">yes or no</span> on some question.', font_size=36).to_edge(UP)
        subtitle = MarkupText(f'We’ll call “yes” <span color="{PLUS_ONE_COLOR}">+1</span> and “no” <span color="{MINUS_ONE_COLOR}">–1</span>.', font_size=30).next_to(title, DOWN, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait()
        
        # --- OBJECTS (unchanged) ---
        alice_circle = Circle(radius=node_radius, color=WHITE, fill_opacity=0.8).move_to(LEFT * 2.5)
        alice_name = Text("Alice", font_size=36).next_to(alice_circle, DOWN, buff=0.3)
        bob_circle = Circle(radius=node_radius, color=WHITE, fill_opacity=0.8).move_to(RIGHT * 2.5)
        bob_name = Text("Bob", font_size=36).next_to(bob_circle, DOWN, buff=0.3)
        up_arrow = Arrow(DOWN*0.2, UP*0.2, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        down_arrow = Arrow(UP*0.2, DOWN*0.2, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        
        # --- INITIAL ANIMATION (unchanged, just shortened for brevity in this view) ---
        self.play(Create(alice_circle), Create(bob_circle), Write(alice_name), Write(bob_name))
        alice_up = up_arrow.copy().move_to(alice_circle.get_center())
        alice_plus_text = MathTex("+1", color=TEXT_COLOR).next_to(alice_circle, UP)
        bob_up = up_arrow.copy().move_to(bob_circle.get_center())
        bob_plus_text = MathTex("+1", color=TEXT_COLOR).next_to(bob_circle, UP)
        self.play(
            alice_circle.animate.set_color(PLUS_ONE_COLOR), Create(alice_up), Write(alice_plus_text),
            bob_circle.animate.set_color(PLUS_ONE_COLOR), Create(bob_up), Write(bob_plus_text)
        )
        self.wait()

        # --- NEW CODE STARTS HERE ---

        # 1. Clean up the scene and reposition
        alice_bob_group = VGroup(
            alice_circle, alice_name, alice_up, alice_plus_text,
            bob_circle, bob_name, bob_up, bob_plus_text
        )
        self.play(
            FadeOut(title, subtitle),
            alice_bob_group.animate.scale(0.9).to_edge(LEFT, buff=1.0)
        )
        self.wait(0.5)

        # 2. Define Table and Status Labels
        table_data = [
            [r"s_1", r"s_2", r"s_1 s_2"],
            [r"+1", r"+1", r"+1"],
            [r"+1", r"-1", r"-1"],
            [r"-1", r"+1", r"-1"],
            [r"-1", r"-1", r"+1"],
        ]
        table = MathTable(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": TEAL},
            h_buff=0.7,
            v_buff=0.4
        ).scale(0.8).next_to(alice_bob_group, RIGHT, buff=1.0)

        status_texts = VGroup(
            MarkupText(f'<span color="{GREEN}">Agree</span>', font_size=28),
            MarkupText(f'<span color="{ORANGE}">Disagree</span>', font_size=28),
            MarkupText(f'<span color="{ORANGE}">Disagree</span>', font_size=28),
            MarkupText(f'<span color="{GREEN}">Agree</span>', font_size=28),
        )

        # 3. Animate the table appearing row-by-row
        header = table.get_rows()[0]
        h_lines = table.get_horizontal_lines()
        v_lines = table.get_vertical_lines()
        
        self.play(Write(header), Create(VGroup(*h_lines, *v_lines)))
        self.wait()

        # Loop through each data row
        for i in range(1, 5):
            s1_val = int(table_data[i][0])
            s2_val = int(table_data[i][1])

            # Define target states for Alice and Bob
            alice_target_arrow = (up_arrow if s1_val == 1 else down_arrow).copy().move_to(alice_circle.get_center())
            alice_target_text = MathTex(f"{s1_val:+}", color=TEXT_COLOR).next_to(alice_circle, UP)
            alice_target_color = PLUS_ONE_COLOR if s1_val == 1 else MINUS_ONE_COLOR

            bob_target_arrow = (up_arrow if s2_val == 1 else down_arrow).copy().move_to(bob_circle.get_center())
            bob_target_text = MathTex(f"{s2_val:+}", color=TEXT_COLOR).next_to(bob_circle, UP)
            bob_target_color = PLUS_ONE_COLOR if s2_val == 1 else MINUS_ONE_COLOR
            
            # Position the status text for this row
            current_status = status_texts[i-1].next_to(table.get_rows()[i], RIGHT, buff=0.5)

            # Animate everything together
            self.play(
                Transform(alice_up, alice_target_arrow),
                Transform(alice_plus_text, alice_target_text),
                alice_circle.animate.set_color(alice_target_color),
                Transform(bob_up, bob_target_arrow),
                Transform(bob_plus_text, bob_target_text),
                bob_circle.animate.set_color(bob_target_color),
                Write(table.get_rows()[i]),
                Write(current_status),
                run_time=1.5
            )
            self.wait(0.5)
        
        self.wait()
        
        # --- NEW SEQUENCE STARTS HERE ---

        # 1. Clean up the previous scene
        all_table_elements = VGroup(table, status_texts)
        self.play(
            FadeOut(alice_bob_group),
            FadeOut(all_table_elements)
        )
        self.wait(0.5)

        # 2. Display the "tension" text
        tension_text = MarkupText(
            'But in the real world, people have a relationship.\n'
            'A <span color="ORANGE">tension</span>, you might say.',
            font_size=36,
            justify=True
        ).move_to(ORIGIN)

        self.play(Write(tension_text))
        self.wait(3) # Pause for narration
        self.play(FadeOut(tension_text))
        self.wait(0.5)

        # 3. Re-create Alice and Bob, more spread out
        alice_circle_new = Circle(radius=node_radius, color=WHITE, fill_opacity=0.8)
        alice_name_new = Text("Alice", font_size=36).next_to(alice_circle_new, DOWN, buff=0.3)
        alice_group_new = VGroup(alice_circle_new, alice_name_new).move_to(LEFT * 3)

        bob_circle_new = Circle(radius=node_radius, color=WHITE, fill_opacity=0.8)
        bob_name_new = Text("Bob", font_size=36).next_to(bob_circle_new, DOWN, buff=0.3)
        bob_group_new = VGroup(bob_circle_new, bob_name_new).move_to(RIGHT * 3)

        self.play(
            Create(alice_group_new),
            Create(bob_group_new)
        )
        self.wait()

        # 4. Add the J_12 label and the segmented connection line
        j_label = MathTex("J_{12}", color=YELLOW).scale(1.2)
        j_label.move_to((alice_circle_new.get_center() + bob_circle_new.get_center()) / 2)

        # Create two separate lines that stop short of the label
        line1 = Line(
            alice_circle_new.get_right(),
            j_label.get_left(),
            buff=0.2,
            color=TEAL,
            stroke_width=3
        )
        line2 = Line(
            j_label.get_right(),
            bob_circle_new.get_left(),
            buff=0.2,
            color=TEAL,
            stroke_width=3
        )
        
        # Animate the appearance of the connection
        self.play(
            Create(line1),
            Create(line2),
            Write(j_label)
        )
        self.wait()

        # --- NEW SEQUENCE STARTS HERE (CORRECTED LAYOUT) ---

        # 1. Group the existing elements and move them to the left
        connection_group = VGroup(alice_group_new, bob_group_new, j_label, line1, line2)
        self.play(
            connection_group.animate.scale(0.9).to_edge(LEFT, buff=1.0)
        )
        self.wait(0.5)

        # 2. Create the VERTICAL J-axis with more ticks
        j_axis = NumberLine(
            x_range=[-1.5, 1.5, 0.5],
            length=5,
            color=WHITE,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
            include_numbers=False 
        )
        
        # Manually add numbers at the default position (below the line)
        j_axis.add_numbers(
            x_values=[-1, 0, 1],
            font_size=32
        )
        
        j_axis.rotate(PI / 2) # Rotate the line and the numbers together
        j_axis.move_to(RIGHT * 2.5)
        
        # --- THIS IS THE FIX ---
        # Now that the axis is vertical, shift the numbers to the LEFT
        j_axis.numbers.shift(LEFT * 0.85)

        j_axis_title = MathTex("J_{12}", "\\text{ dial}", color=YELLOW).next_to(j_axis, UP)
        j_axis_title[1].set_color(WHITE)

        self.play(Create(j_axis), Write(j_axis_title))
        self.wait()

        # 3. Create the simplified descriptive labels
        positive_label = MarkupText(
            f'<span color="{RED_E}">Tense</span>', font_size=34
        ).next_to(j_axis.n2p(1), RIGHT, buff=0.4)

        negative_label = MarkupText(
            f'<span color="{BLUE_E}">Cozy</span>', font_size=34
        ).next_to(j_axis.n2p(-1), RIGHT, buff=0.4)

        zero_label = MarkupText(
            'No influence', font_size=34
        ).next_to(j_axis.n2p(0), RIGHT, buff=0.4)

        # 4. Animate the explanations sequentially with a pointer dot
        dot = Dot(color=YELLOW).scale(1.2)

        # J > 0 (Tense)
        dot.move_to(j_axis.n2p(1))
        self.play(FadeIn(dot, scale=0.5), Write(positive_label))
        self.wait(1.5)

        # J < 0 (Cozy)
        self.play(
            dot.animate.move_to(j_axis.n2p(-1)),
            Write(negative_label)
        )
        self.wait(1.5)

        # J = 0 (No influence)
        self.play(
            dot.animate.move_to(j_axis.n2p(0)),
            Write(zero_label)
        )
        self.wait(1.5)
        
        # 5. Fade out the dial and get ready for the next part
        j_dial_group = VGroup(j_axis, j_axis.numbers, j_axis_title, positive_label, negative_label, zero_label, dot)
        self.play(FadeOut(j_dial_group))
        
        self.add(connection_group) 
        self.wait()

        # (This code follows immediately after the FadeOut of the first j_dial_group)
        # The 'connection_group' Mobject is still present on the screen.
        
        # --- NEW SEQUENCE STARTS HERE (CORRECTED WITH SMOOTH MOVEMENT) ---

        # --- PART 1: DEFINE ALL OBJECTS AND CALCULATE FINAL LAYOUT ---

        # A) Create a target copy of the diagram to calculate its final position
        target_connection_group = connection_group.copy()
        target_connection_group.scale(0.9).to_edge(UP, buff=1.0)

        # B) Left Panel: Formulas (we won't show them yet)
        desc_font_size = 28
        desc_part1 = MarkupText(f'<span color="{H_COLOR}">Conflict</span> = <span color="{PLUS_ONE_COLOR}">Alice\'s choice</span> × <span color="{J_COLOR}">Tension</span> × ', font_size=desc_font_size)
        desc_bob_choice = MarkupText(f'<span color="{PLUS_ONE_COLOR}">Bob\'s choice</span>', font_size=desc_font_size)
        desc_formula = VGroup(desc_part1, desc_bob_choice).arrange(RIGHT, buff=0.1)
        math_formula = MathTex("H", "=", "s_1", "J_{12}", "s_2", tex_to_color_map={"H": H_COLOR, "s_1": PLUS_ONE_COLOR, "J_{12}": J_COLOR, "s_2": PLUS_ONE_COLOR}).scale(1.2)
        formulas_group = VGroup(desc_formula, math_formula).arrange(DOWN, buff=0.4)
        
        # We use the INVISIBLE target_connection_group to define the layout
        left_panel = VGroup(target_connection_group, formulas_group).arrange(DOWN, buff=0.7)

        # C) Right Panel: Dials
        dial_config = {"x_range": [-1.5, 1.5, 0.5], "length": 3.5, "include_numbers": False, "rotation": PI/2}
        j_dial = NumberLine(**dial_config)
        j_dial.add_numbers(x_values=[-1, 0, 1], font_size=24).numbers.shift(LEFT * 0.4)
        j_dial_title = MathTex("J_{12}", color=J_COLOR).next_to(j_dial, UP)
        j_dial_group = VGroup(j_dial, j_dial.numbers, j_dial_title)
        h_dial = NumberLine(**dial_config)
        h_dial.add_numbers(x_values=[-1, 0, 1], font_size=24).numbers.shift(LEFT * 0.4)
        h_dial_title = MathTex("H", color=H_COLOR).next_to(h_dial, UP)
        h_dial_group = VGroup(h_dial, h_dial.numbers, h_dial_title)
        right_panel = VGroup(j_dial_group, h_dial_group).arrange(0.9*RIGHT, buff=1)
        
        # D) Arrange the panels on screen to ensure they fit and are centered
        main_layout = VGroup(left_panel, right_panel).arrange(RIGHT, buff=1.5).move_to(ORIGIN)

        # --- PART 2: ANIMATE IN THE CORRECT ORDER ---

        # 1. Move the original, visible diagram to its new position
        self.play(
            Transform(connection_group, target_connection_group)
        )
        self.wait(1)
        
        # 2. Bring in the dials
        self.play(Create(right_panel))
        self.wait(1)
        
        # 3. Bring in the formulas
        self.play(Write(formulas_group))
        self.wait(1)

        # --- PART 3: DEMONSTRATION WITH LIVE CALCULATION ---
        
        s1_val, s2_val, j_val = 1, 1, -1

        def get_calc_text(s1, j, s2):
            h = s1 * j * s2
            text = MathTex("H", "=", f"({s1:+})", r"\times", f"({j:+})", r"\times", f"({s2:+})", "=", f"{h:+.0f}").scale(1.1)
            text.next_to(math_formula, DOWN, buff=0.4)
            text[0].set_color(H_COLOR)
            text[2].set_color(PLUS_ONE_COLOR if s1 > 0 else MINUS_ONE_COLOR)
            text[4].set_color(J_COLOR)
            text[6].set_color(PLUS_ONE_COLOR if s2 > 0 else MINUS_ONE_COLOR)
            text[8].set_color(H_COLOR)
            return text

        # We must now reference the sub-parts of the transformed connection_group
        alice_circle = connection_group.submobjects[0].submobjects[0]
        bob_circle = connection_group.submobjects[1].submobjects[0]
        up_arrow = Arrow(DOWN*0.2, UP*0.2, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        down_arrow = Arrow(UP*0.2, DOWN*0.2, stroke_width=3, max_tip_length_to_length_ratio=0.35)
        alice_spin = up_arrow.copy().move_to(alice_circle.get_center())
        bob_spin = up_arrow.copy().move_to(bob_circle.get_center())
        
        j_dot = Dot(color=J_COLOR, radius=0.1).move_to(j_dial.n2p(j_val))
        h_dot = Dot(color=H_COLOR, radius=0.1).move_to(h_dial.n2p(s1_val * j_val * s2_val))
        calculation_text = get_calc_text(s1_val, j_val, s2_val)

        self.play(
            Create(alice_spin), Create(bob_spin),
            alice_circle.animate.set_color(PLUS_ONE_COLOR),
            bob_circle.animate.set_color(PLUS_ONE_COLOR),
            FadeIn(j_dot), FadeIn(h_dot),
            Write(calculation_text)
        )
        self.wait(2)
        # (The rest of the demonstration remains the same)
        s2_val = -1
        new_calc = get_calc_text(s1_val, j_val, s2_val)
        new_bob_spin = down_arrow.copy().move_to(bob_circle.get_center())
        self.play(
            bob_circle.animate.set_color(MINUS_ONE_COLOR),
            Transform(bob_spin, new_bob_spin),
            h_dot.animate.move_to(h_dial.n2p(s1_val * j_val * s2_val)),
            FadeToColor(math_formula[4], MINUS_ONE_COLOR),
            desc_bob_choice.animate.set_color(MINUS_ONE_COLOR), 
            Transform(calculation_text, new_calc), run_time=1.5
        )
        self.wait(2)

        j_val = 1
        new_calc = get_calc_text(s1_val, j_val, s2_val)
        self.play(
            j_dot.animate.move_to(j_dial.n2p(j_val)),
            h_dot.animate.move_to(h_dial.n2p(s1_val * j_val * s2_val)),
            Transform(calculation_text, new_calc), run_time=1.5
        )
        self.wait(2)

        s2_val = 1
        new_calc = get_calc_text(s1_val, j_val, s2_val)
        new_bob_spin_up = up_arrow.copy().move_to(bob_circle.get_center())
        self.play(
            bob_circle.animate.set_color(PLUS_ONE_COLOR),
            Transform(bob_spin, new_bob_spin_up),
            h_dot.animate.move_to(h_dial.n2p(s1_val * j_val * s2_val)),
            FadeToColor(math_formula[4], PLUS_ONE_COLOR),
            desc_bob_choice.animate.set_color(PLUS_ONE_COLOR),
            Transform(calculation_text, new_calc), run_time=1.5
        )
        self.wait(3)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: FINDING THE GROUND STATE (CORRECTED DIAGRAM) ---
        
        # --- PART 1: CLEANUP AND RECAP ---
        
        all_previous_mobjects = VGroup(
            connection_group, right_panel, formulas_group,
            calculation_text, alice_spin, bob_spin, j_dot, h_dot
        )
        self.play(FadeOut(all_previous_mobjects))
        self.wait(0.5)

        DEFAULT_FONT_SIZE = 32
        recap_text = MarkupText(
            "The 'Conflict' depends on their choices and the 'Tension' between them.",
            font_size=DEFAULT_FONT_SIZE
        )
        self.play(Write(recap_text))
        self.wait(2)

        # --- PART 2: POSE THE QUESTION ---

        question_text_1 = Text("Now, let's assume the tension J is fixed.", font_size=DEFAULT_FONT_SIZE)
        question_text_2 = MarkupText(f'The question is: what choices will they make to <span color="{H_COLOR}">minimize the conflict</span>?', font_size=DEFAULT_FONT_SIZE)
        question_text_3 = MarkupText(f'This lowest-energy state is called the <span color="{YELLOW}">ground state</span>.', font_size=DEFAULT_FONT_SIZE)
        question_group = VGroup(question_text_1, question_text_2, question_text_3).arrange(DOWN, buff=0.4)

        self.play(ReplacementTransform(recap_text, question_group))
        self.wait(4)
        self.play(FadeOut(question_group))
        self.wait(0.5)

        # --- PART 3: THE INTERACTIVE TABLE ---
