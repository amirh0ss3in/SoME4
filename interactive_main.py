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

        # --- PART 3: THE INTERACTIVE TABLE (REWRITTEN WITH CORRECT BUFFERS AND SPACING) ---

        # A) Setup the main components
        case_label = MathTex("J_{12}", "=", "?").scale(1.5).to_edge(UP, buff=1.0)

        table = MathTable(
            [["+1","+1",""],["+1","-1",""],["-1","+1",""],["-1","-1",""]],
            col_labels=[MathTex("s_1"), MathTex("s_2"), MathTex("H", color=H_COLOR)],
            include_outer_lines=True
        ).scale(0.9).next_to(case_label, DOWN, buff=0.7)

        # Helper function to create the s_gs vector display
        def create_gs_vector(s1, s2):
            s_gs_label = MathTex("s_{gs}", "=").set_color(YELLOW)
            s1_val_text = MathTex(f"{s1:+}").set_color(WHITE)
            s2_val_text = MathTex(f"{s2:+}").set_color(WHITE)
            
            vector_body = VGroup(
                MathTex("["), s1_val_text, s2_val_text, MathTex("]")
            ).arrange(RIGHT, buff=0.25)
            
            full_vector = VGroup(s_gs_label, vector_body).arrange(RIGHT, buff=0.3)
            return full_vector

        # B) Animate the appearance of the tools
        self.play(Write(case_label))
        self.play(Create(table))
        self.wait(1)

        # C) Case 1: J = -1 ("Cozy")
        j_val_cozy = -1
        new_case_label_cozy = MathTex("J_{12}", "=", f"{j_val_cozy}").scale(1.5).move_to(case_label)
        new_case_label_cozy[0].set_color(J_COLOR)
        new_case_label_cozy[2].set_color(PLUS_ONE_COLOR)
        
        s1_vals = [int(c.get_tex_string()) for c in table.get_columns()[0][1:]]
        s2_vals = [int(c.get_tex_string()) for c in table.get_columns()[1][1:]]
        h_col_data_cozy = VGroup(*[MathTex(f"{j_val_cozy * s1 * s2}", color=H_COLOR) for s1, s2 in zip(s1_vals, s2_vals)]).scale(0.9)
        for i, item in enumerate(h_col_data_cozy):
            item.move_to(table.get_cell((i+2, 3)))

        self.play(Transform(case_label, new_case_label_cozy))
        self.play(Write(h_col_data_cozy))
        self.wait(1)
        
        # Point to the first ground state with correct spacing
        gs1_row = table.get_rows()[1]
        gs_vector_display = create_gs_vector(1, 1).next_to(gs1_row, LEFT, buff=1.5)
        pointer = Arrow(
            start=gs_vector_display.get_right() + RIGHT * 0.4, # Add gap on the left
            end=gs1_row.get_left() + LEFT * 0.1,             # Add gap on the right
            color=YELLOW
        )

        self.play(Write(gs_vector_display), GrowArrow(pointer))
        self.wait(2)

        # Move to the second ground state
        gs2_row = table.get_rows()[4]
        target_vector = create_gs_vector(-1, -1).next_to(gs2_row, LEFT, buff=1.5)
        target_pointer = Arrow(
            start=target_vector.get_right() + RIGHT * 0.4, # Add gap on the left
            end=gs2_row.get_left() + LEFT * 0.1,             # Add gap on the right
            color=YELLOW
        )

        self.play(
            Transform(pointer, target_pointer),
            Transform(gs_vector_display, target_vector)
        )
        self.wait(2)

        # D) Case 2: J = +1 ("Tense")
        self.play(FadeOut(pointer), FadeOut(gs_vector_display))
        j_val_tense = 1
        new_case_label_tense = MathTex("J_{12}", "=", f"+{j_val_tense}").scale(1.5).move_to(case_label)
        new_case_label_tense[0].set_color(J_COLOR)
        new_case_label_tense[2].set_color(MINUS_ONE_COLOR)
        
        h_col_data_tense = VGroup(*[MathTex(f"{j_val_tense * s1 * s2}", color=H_COLOR) for s1, s2 in zip(s1_vals, s2_vals)]).scale(0.9)
        for i, item in enumerate(h_col_data_tense):
            item.move_to(table.get_cell((i+2, 3)))

        self.play(
            Transform(case_label, new_case_label_tense),
            Transform(h_col_data_cozy, h_col_data_tense),
            run_time=1.5
        )
        self.wait(1)

        # Point to the new ground states with correct spacing
        gs1_row_new = table.get_rows()[2]
        gs_vector_display = create_gs_vector(1, -1).next_to(gs1_row_new, LEFT, buff=1.5)
        pointer = Arrow(
            start=gs_vector_display.get_right() + RIGHT * 0.4, # Add gap on the left
            end=gs1_row_new.get_left() + LEFT * 0.1,             # Add gap on the right
            color=YELLOW
        )
        
        self.play(Write(gs_vector_display), GrowArrow(pointer))
        self.wait(2)
        
        gs2_row_new = table.get_rows()[3]
        target_vector = create_gs_vector(-1, 1).next_to(gs2_row_new, LEFT, buff=1.5)
        target_pointer = Arrow(
            start=target_vector.get_right() + RIGHT * 0.4, # Add gap on the left
            end=gs2_row_new.get_left() + LEFT * 0.1,             # Add gap on the right
            color=YELLOW
        )

        self.play(
            Transform(pointer, target_pointer),
            Transform(gs_vector_display, target_vector)
        )
        self.wait(3)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: THREE PEOPLE (FINAL POLISHED VERSION) ---
        
        # 1. Clean up all elements from the previous scene
        all_table_elements = VGroup(case_label, table, h_col_data_cozy, pointer, gs_vector_display)
        self.play(FadeOut(all_table_elements))
        self.wait(0.5)

        # 2. Pose the question
        question_text = Text("You might wonder... what happens with three people?", font_size=36)
        self.play(Write(question_text))
        self.wait(2)
        self.play(FadeOut(question_text))
        self.wait(0.5)

        # 3. Define helper functions with corrected, robust logic
        node_radius = 0.3

        def create_person(name, position):
            circle = Circle(radius=node_radius, color=WHITE, fill_opacity=0.8)
            text_name = Text(name, font_size=36).next_to(circle, DOWN, buff=0.2)
            # Ensure names are drawn on top of lines
            text_name.set_z_index(2)
            # Add a background to prevent lines from cutting through the text
            text_name.add_background_rectangle(opacity=1, buff=0.05)
            return VGroup(circle, text_name).move_to(position)

        def create_connection(node1, node2, label_text):
            circle1 = node1.submobjects[0]
            circle2 = node2.submobjects[0]
            p1, p2 = circle1.get_center(), circle2.get_center()
            direction_vector = p2 - p1
            unit_direction = direction_vector / np.linalg.norm(direction_vector)
            line = Line(p1 + unit_direction * node_radius, p2 - unit_direction * node_radius, z_index=-1, color=TEAL, stroke_width=3)
            label = MathTex(label_text, color=J_COLOR).scale(1.2)
            label.move_to(line.get_center())
            line_angle = line.get_angle()
            label.rotate(line_angle)
            if (PI / 2) < abs(line_angle) < (3 * PI / 2):
                label.rotate(PI)
            label.add_background_rectangle(opacity=1, buff=0.1)
            return VGroup(line, label)

        # 4. Define the nodes in a triangle layout
        alice_node = create_person("Alice", UP * 2.2)
        bob_node = create_person("Bob", DOWN * 1.5 + LEFT * 2.5)
        charlie_node = create_person("Charlie", DOWN * 1.5 + RIGHT * 2.5)
        
        all_nodes = VGroup(alice_node, bob_node, charlie_node)
        self.play(Create(all_nodes))
        self.wait(1)

        # 5. Define and animate the connections using the new, smooth technique
        connection_12 = create_connection(alice_node, bob_node, "J_{12}")
        connection_13 = create_connection(alice_node, charlie_node, "J_{13}")
        connection_23 = create_connection(bob_node, charlie_node, "J_{23}")

        self.play(
            LaggedStart(
                Create(connection_12),
                Create(connection_13),
                Create(connection_23),
                lag_ratio=0.6, # Start the next animation when the previous is 60% done
                run_time=3     # The entire process takes 3 seconds
            )
        )
        self.wait(3)
    
        # (This code follows immediately after the previous sequence ends)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: BUILDING THE HAMILTONIAN (DEFINITIVE CORRECTED VERSION) ---

        # 1. Group the entire system and move it to the left
        triangle_system = VGroup(all_nodes, connection_12, connection_13, connection_23)
        self.play(
            triangle_system.animate.scale(0.8).to_edge(LEFT, buff=1.0)
        )
        self.wait(0.5)

        # 2. Define the position for the formulas to appear on the right
        formula_pos = RIGHT * 3.0

        # 3. Create and animate the individual conflict formulas
        
        h12_formula = MathTex("H_{12}", "=", "s_1", "J_{12}", "s_2", tex_to_color_map={"H_{12}": H_COLOR, "J_{12}": J_COLOR}).scale(1.2).move_to(formula_pos)
        self.play(Write(h12_formula))
        self.wait(1.5)
        self.play(FadeOut(h12_formula))

        h13_formula = MathTex("H_{13}", "=", "s_1", "J_{13}", "s_3", tex_to_color_map={"H_{13}": H_COLOR, "J_{13}": J_COLOR}).scale(1.2).move_to(formula_pos)
        self.play(Write(h13_formula))
        self.wait(1.5)
        self.play(FadeOut(h13_formula))

        h23_formula = MathTex("H_{23}", "=", "s_2", "J_{23}", "s_3", tex_to_color_map={"H_{23}": H_COLOR, "J_{23}": J_COLOR}).scale(1.2).move_to(formula_pos)
        self.play(Write(h23_formula))
        self.wait(2)

        # 4. Reveal the total Hamiltonian in a two-line format with a title
        
        # Create each part of the equation separately
        h_total_label = MathTex("H", "=").set_color_by_tex("H", H_COLOR)
        term1 = MathTex("s_1 J_{12} s_2").set_color_by_tex("J", J_COLOR)
        plus_sign = MathTex("+").set_color(WHITE)
        term2 = MathTex("s_1 J_{13} s_3").set_color_by_tex("J", J_COLOR)
        term3 = MathTex("+ s_2 J_{23} s_3").set_color_by_tex("J", J_COLOR)
        
        # Arrange the first line
        line1 = VGroup(h_total_label, term1, plus_sign, term2).arrange(RIGHT, buff=0.2)
        
        # Position the second line (term3) aligned under the start of term1
        term3.next_to(line1, DOWN, buff=0.2, aligned_edge=LEFT)
        term3.align_to(term1, LEFT)
        
        # Group the formula parts
        full_formula = VGroup(line1, term3)
        
        # --- NEW --- Create the title and group it with the formula
        total_conflict_title = Text("Total Conflict", font_size=36)
        n3_hamiltonian_group = VGroup(total_conflict_title, full_formula).arrange(DOWN, buff=0.4)
        n3_hamiltonian_group.move_to(formula_pos)

        self.play(ReplacementTransform(h23_formula, n3_hamiltonian_group))
        self.wait(4)
        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: GENERALIZING TO N=4 AND THE SUMMATION (REVISED) ---

        # 1. Modify the connection helper to prevent label overlap
        def create_connection(node1, node2, label_text, label_pos_alpha=0.5):
            circle1 = node1.submobjects[0]
            circle2 = node2.submobjects[0]
            p1, p2 = circle1.get_center(), circle2.get_center()
            direction_vector = p2 - p1
            unit_direction = direction_vector / np.linalg.norm(direction_vector)
            
            line = Line(
                p1 + unit_direction * node_radius, 
                p2 - unit_direction * node_radius, 
                z_index=-1, color=TEAL, stroke_width=3
            )
            label = MathTex(label_text, color=J_COLOR).scale(1.2)
            label.move_to(line.point_from_proportion(label_pos_alpha))
            
            line_angle = line.get_angle()
            label.rotate(line_angle)
            if (PI / 2) < abs(line_angle) < (3 * PI / 2):
                label.rotate(PI)
            label.add_background_rectangle(opacity=1, buff=0.1)
            return VGroup(line, label)

        # 2. Prepare the N=4 system and the new Hamiltonian layout
        
        # A. Create the N=4 graph nodes
        alice_node_sq = create_person("Alice", UP * 2.0 + LEFT * 2.0)
        bob_node_sq = create_person("Bob", UP * 2.0 + RIGHT * 2.0)
        charlie_node_sq = create_person("Charlie", DOWN * 2.0 + LEFT * 2.0)
        diana_node = create_person("Diana", DOWN * 2.0 + RIGHT * 2.0)
        all_nodes_n4 = VGroup(alice_node_sq, bob_node_sq, charlie_node_sq, diana_node)

        # B. Create N=4 connections, offsetting diagonal labels to avoid overlap
        connections_n4 = VGroup(
            create_connection(alice_node_sq, bob_node_sq, "J_{12}"),
            create_connection(charlie_node_sq, diana_node, "J_{34}"),
            create_connection(alice_node_sq, charlie_node_sq, "J_{13}"),
            create_connection(bob_node_sq, diana_node, "J_{24}"),
            create_connection(alice_node_sq, diana_node, "J_{14}", label_pos_alpha=0.6), # Offset
            create_connection(bob_node_sq, charlie_node_sq, "J_{23}", label_pos_alpha=0.4)  # Offset
        )
        n4_system = VGroup(all_nodes_n4, connections_n4).scale(0.8).to_edge(LEFT, buff=1.0)
        
        # C. Define the target N=4 Hamiltonian formula with its title
        total_conflict_title_n4 = Text("Total Conflict", font_size=36)
        
        h_total_label = MathTex("H", "=").set_color_by_tex("H", H_COLOR)
        terms = [MathTex(t) for t in ["s_1 J_{12} s_2", "+ s_1 J_{13} s_3", "+ s_2 J_{23} s_3", "+ s_1 J_{14} s_4", "+ s_2 J_{24} s_4", "+ s_3 J_{34} s_4"]]
        for term in terms:
            term.set_color_by_tex("J", J_COLOR)
            
        line1_n4 = VGroup(*terms[:3]).arrange(RIGHT, buff=0.15)
        line2_n4 = VGroup(*terms[3:]).arrange(RIGHT, buff=0.15)
        
        n4_formula_terms = VGroup(line1_n4, line2_n4).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        n4_formula_body = VGroup(h_total_label, n4_formula_terms).arrange(RIGHT, buff=0.2)
        
        n4_hamiltonian_group = VGroup(total_conflict_title_n4, n4_formula_body).arrange(DOWN, buff=0.4)
        n4_hamiltonian_group.scale(0.8).move_to(RIGHT * 3.0)

        # 3. Animate the transformation from the N=3 system to the N=4 system
        all_n3_objects = VGroup(triangle_system, n3_hamiltonian_group)
        
        self.play(
            ReplacementTransform(all_n3_objects, VGroup(n4_system, n4_hamiltonian_group)),
            run_time=2.5
        )
        self.wait(3)

        # 4. Reveal the final, general formula
        summation_formula = MathTex(r"H = \sum_{i<j} s_i J_{ij} s_j", font_size=60)
        summation_formula.set_color_by_tex_to_color_map({
            "H": H_COLOR,
            "J_{ij}": J_COLOR
        })
        summation_formula.move_to(n4_hamiltonian_group.get_center())

        self.play(
            ReplacementTransform(n4_hamiltonian_group, summation_formula),
            n4_system.animate.fade(0.7)
        )
        self.wait(5)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: THE MATRIX FORMULATION ---

        # 1. Clean up the scene, leaving only the summation formula
        self.play(
            FadeOut(n4_system),
            summation_formula.animate.move_to(ORIGIN).scale(1.2)
        )
        self.wait(1)

        # 2. Define the components: s_i and J
        s_i_def = MathTex(r"s_i \in \{+1, -1\}", font_size=36)
        j_matrix_def = MarkupText(
            f'J is an <span color="{J_COLOR}">N × N</span> matrix of tensions', 
            font_size=36
        )
        
        definitions_group = VGroup(s_i_def, j_matrix_def).arrange(DOWN, buff=0.5)
        definitions_group.next_to(summation_formula, DOWN, buff=1.0)
        
        self.play(Write(definitions_group))
        self.wait(3)

        # 3. Introduce the symmetry argument
        symmetry_text = MarkupText(
            f'In the real world, the tension is mutual: <span color="{YELLOW}">J<sub>ij</sub> = J<sub>ji</sub></span>',
            font_size=42
        )
        symmetry_text.move_to(definitions_group)

        self.play(ReplacementTransform(definitions_group, symmetry_text))
        self.wait(3)

        # 4. Rewrite the formula into its final matrix-ready form
        final_formula = MathTex(r"H = \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} s_i J_{ij} s_j", font_size=60)
        final_formula.set_color_by_tex_to_color_map({
            "H": H_COLOR,
            "J_{ij}": J_COLOR
        })
        final_formula.move_to(summation_formula)

        n_explanation = MarkupText(
            "where N is the number of people (spins)", 
            font_size=32
        ).next_to(final_formula, DOWN, buff=0.7)

        self.play(
            ReplacementTransform(summation_formula, final_formula),
            ReplacementTransform(symmetry_text, n_explanation),
            run_time=2
        )
        self.wait(5)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: THE MATRIX-VECTOR FORM (REVISED LAYOUT) ---

        # 1. Clean up the explanation text
        self.play(FadeOut(n_explanation))
        self.wait(0.5)

        # 2. Transform the summation formula into the compact matrix form
        sTJs_formula = MathTex(r"H = \frac{1}{2} \mathbf{s}^T \mathbf{J} \mathbf{s}", font_size=60)
        sTJs_formula.set_color_by_tex_to_color_map({
            "H": H_COLOR,
            r"\mathbf{J}": J_COLOR,
            r"\mathbf{s}": PLUS_ONE_COLOR
        })
        sTJs_formula.move_to(final_formula)

        self.play(ReplacementTransform(final_formula, sTJs_formula))
        self.wait(2)

        # 3. Animate the main formula moving up to become a "title" for the explanation
        self.play(
            sTJs_formula.animate.scale(0.8).to_edge(UP, buff=1.0)
        )
        self.wait(0.5)

        # 4. Show what s^T J s means visually in the newly cleared space
        
        # --- THIS IS THE FIX ---
        # A. Create the components for s^T, J, and s more robustly
        s1_tex = MathTex("s_1")
        s2_tex = MathTex("s_2")
        dots_tex = MathTex(r"\dots")
        sN_tex = MathTex("s_N")
        s_T_vec = VGroup(
            MathTex("["), s1_tex, s2_tex, dots_tex, sN_tex, MathTex("]")
        ).arrange(RIGHT, buff=0.2).set_color(PLUS_ONE_COLOR)
        
        j_matrix = Matrix(
            [[r"J_{11}", r"J_{12}", r"\dots", r"J_{1N}"],
             [r"J_{21}", r"J_{22}", r"\dots", r"J_{2N}"],
             [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
             [r"J_{N1}", r"J_{N2}", r"\dots", r"J_{NN}"]],
            h_buff=1.2, v_buff=0.7, bracket_h_buff=0.2
        ).set_color(J_COLOR)
        
        s_vec = Matrix(
            [[r"s_1"], [r"s_2"], [r"\vdots"], [r"s_N"]]
        ).set_color(PLUS_ONE_COLOR)
        
        one_half = MathTex(r"\frac{1}{2}")

        # B. Group and arrange them in the center of the screen
        expanded_form = VGroup(one_half, s_T_vec, j_matrix, s_vec).arrange(RIGHT, buff=0.25)
        expanded_form.scale(0.8).move_to(ORIGIN)

        # C. Animate their appearance
        self.play(
            LaggedStart(
                Write(one_half),
                Write(s_T_vec),
                Create(j_matrix),
                Write(s_vec),
                lag_ratio=0.5
            )
        )
        self.wait(5)

        # (This code follows immediately after the previous sequence ends)

        # --- NEW SEQUENCE: THE COMPLEXITY OF FINDING THE GROUND STATE (POLISHED VERSION) ---

        # --- PART 1: Posing the Problem (The "Brute-Force" Approach) ---

        # 1. Cleanup and focus on the spin vector
        self.play(
            FadeOut(one_half, j_matrix, s_vec), # Fade out everything except s^T vector and title
            sTJs_formula.animate.fade(0.5)      # Dim the title
        )
        # s_T_vec is the horizontal vector from the previous scene
        
        # FIX: Add the "s^T =" label to the vector
        s_T_label = MathTex(r"\mathbf{s}^T =").scale(1.5).set_color(PLUS_ONE_COLOR)
        labeled_s_vector = VGroup(s_T_label, s_T_vec).arrange(RIGHT, buff=0.25)

        self.play(labeled_s_vector.animate.move_to(ORIGIN))
        self.wait(1)

        # 2. Pose the question
        # FIX: Reduce font size and justify text to prevent overflow
        question = MarkupText(
            "To find the ground state, which configuration of spins minimizes H?",
            font_size=32,
            justify=True
        ).next_to(labeled_s_vector, UP, buff=1.0)
        self.play(Write(question))
        self.wait(2)

        # 3. Count the choices for each spin
        s1 = s_T_vec.submobjects[1]
        s2 = s_T_vec.submobjects[2]
        sN = s_T_vec.submobjects[4]

        # FIX: Increase buff for a slightly larger highlight box
        highlight_box = SurroundingRectangle(s1, color=YELLOW, buff=0.15)
        choices_text = MarkupText("2 choices (+1 or –1)", font_size=28).next_to(labeled_s_vector, DOWN, buff=0.7)
        self.play(Create(highlight_box), Write(choices_text))
        self.wait(1)

        self.play(highlight_box.animate.move_to(s2))
        self.wait(0.5)
        self.play(highlight_box.animate.move_to(sN))
        self.wait(1)

        # 4. Build the 2^N formula from the choices
        multiplication_text = MathTex("2 \\times 2 \\times \\dots \\times 2", font_size=48)
        n_times_label = MathTex("(N \\text{ times})", font_size=36).next_to(multiplication_text, DOWN)
        multiplication_group = VGroup(multiplication_text, n_times_label).move_to(choices_text.get_center())
        
        self.play(ReplacementTransform(choices_text, multiplication_group))
        self.wait(2)

        # FIX: Use MathTex with \text{} to ensure proper spacing
        final_configs_formula = MathTex(r"\text{Total Configurations} = 2^N", font_size=48)
        final_configs_formula.move_to(multiplication_group.get_center())
        
        self.play(
            ReplacementTransform(multiplication_group, final_configs_formula),
            FadeOut(question, labeled_s_vector, highlight_box, sTJs_formula)
        )
        self.wait(1)

        # --- PART 2: Visualizing Exponential Growth (Linear Scale) ---

        # 1. Set the stage for the graph
        self.play(final_configs_formula.animate.scale(0.7).to_edge(UP, buff=0.5))
        
        # FIX: Use a linear scale, we will move the graph to keep the dot in view.
        ax = Axes(
            x_range=[0, 32, 5],
            y_range=[0, 40, 10], # Start with a small, manageable y-range
            x_length=10,
            y_length=5.5, # Make y-axis a bit shorter to give more vertical room
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 31, 5)},
        )

        x_label = ax.get_x_axis_label("N \\text{ (Number of People)}")
        y_label = ax.get_y_axis_label("\\text{Configurations}", edge=LEFT, direction=UP)
        y_label.next_to(ax.y_axis, UP, buff=0.2)
        
        # FIX: Group everything and scale it down slightly to fit well
        graph_group = VGroup(ax, x_label, y_label).scale(0.95).move_to(ORIGIN)
        self.play(Create(graph_group))
        self.wait(1)

        # 2. Plot the curve and animate its explosive growth
        tracker = ValueTracker(2)
        
        # Create a graph that will be updated
        graph = ax.plot(lambda x: 2**x, color=WHITE, x_range=[0,2])

        # Create a dot that tracks the end of the graph
        dot = Dot(color=YELLOW).move_to(graph.get_end())
        
        # Create a label for the dot
        label = always_redraw(lambda: 
            MathTex(f"2^{{{int(tracker.get_value())}}} = {int(2**tracker.get_value()):,}")
            .scale(0.7).next_to(dot, UR, buff=0.1)
        )

        self.play(Create(graph), FadeIn(dot), FadeIn(label))
        self.wait(1)

        # Animate to N=5
        self.play(
            tracker.animate.set_value(5),
            UpdateFromFunc(graph, lambda m: m.become(ax.plot(lambda x: 2**x, color=WHITE, x_range=[0, 5]))),
            UpdateFromFunc(dot, lambda m: m.move_to(ax.c2p(5, 2**5))),
            run_time=2
        )
        self.wait(1)
        
        # Animate to N=10, moving the graph down to keep the dot in frame
        self.play(
            tracker.animate.set_value(10),
            UpdateFromFunc(graph, lambda m: m.become(ax.plot(lambda x: 2**x, color=WHITE, x_range=[0, 10]))),
            # Animate the dot and the entire graph group simultaneously
            dot.animate.move_to(ax.c2p(10, 2**10)),
            graph_group.animate.shift(DOWN * 3),
            run_time=3
        )
        self.wait(1)
        
        # Animate to N=30, showing the massive jump
        self.play(
            tracker.animate.set_value(30),
            # We don't need to draw the full graph, just move the dot to its final position
            # while the graph scrolls away, creating a sense of immense scale.
            dot.animate.move_to(ax.c2p(30, 2**30)), 
            graph_group.animate.shift(DOWN * 20), # Move graph way off-screen
            run_time=4
        )
        self.wait(2)


        # --- PART 3: The "Impossible" Punchline ---
        
        # 1. Clean up the graph elements
        self.play(
            FadeOut(graph_group, dot, label, graph, final_configs_formula)
        )
        self.wait(0.5)

        # 2. Show the N=300 case
        n300_text = MathTex("N = 300", font_size=72)
        self.play(Write(n300_text))
        self.wait(1)

        # 3. Create the punchline text
        line1 = MarkupText(
            "For just 300 people, the number of configurations (2<sup>300</sup>)...", 
            font_size=36
        )
        
        # --- THIS IS THE FIX ---
        # Create each line of the final sentence as a separate object
        line2a = MarkupText(
            "is greater than the number of atoms", 
            font_size=42, color=YELLOW
        )
        line2b = MarkupText(
            "in the known universe.",
            font_size=42, color=YELLOW
        )
        # Arrange them in a VGroup, which will center them by default
        line2_group = VGroup(line2a, line2b).arrange(DOWN, buff=0.2)
        
        # Group the entire punchline for positioning
        punchline = VGroup(line1, line2_group).arrange(DOWN, buff=0.5)
        
        # 4. Animate the final text
        self.play(
            n300_text.animate.next_to(punchline, UP, buff=0.7)
        )
        self.play(Write(line1))
        self.wait(1.5)
        # Write the two-line group together
        self.play(Write(line2_group))
        self.wait(5)


class LinkToNPHardness(Scene):
    def construct(self):
        # --- CONFIGURATION (from previous scene) ---
        PLUS_ONE_COLOR = BLUE_D
        MINUS_ONE_COLOR = RED_D
        TEXT_COLOR = YELLOW
        J_COLOR = YELLOW
        H_COLOR = GREEN
        
        # --- SEQUENCE 1: INTRO AND WHY WE CARE ---
        
        title_text = MarkupText(
            'Why is this <span color="YELLOW">Ising Problem</span> important?',
            font_size=42
        )
        subtitle_text = MarkupText(
            "It's a <span color='TEAL'>universal puzzle</span> that describes many other hard problems.",
            font_size=36
        ).next_to(title_text, DOWN, buff=0.4)

        self.play(Write(title_text))
        self.wait(2)
        self.play(Write(subtitle_text))
        self.wait(3)
        self.play(FadeOut(title_text, subtitle_text))
        self.wait(0.5)

        # --- SEQUENCE 2: THE NUMBER PARTITIONING PROBLEM ---
        
        problem_title = Text("The Number Partitioning Problem", font_size=38).to_edge(UP)
        self.play(Write(problem_title))
        self.wait(1)

        numbers_list = [8, 7, 6, 5]
        numbers_tex = VGroup(*[MathTex(str(n)) for n in numbers_list]).arrange(RIGHT, buff=0.8).scale(0.9)
        self.play(Write(numbers_tex))
        self.wait(2)

        # --- FIX #1: Move numbers up to make space for the bins ---
        self.play(numbers_tex.animate.to_edge(UP, buff=2.0))
        self.wait(0.5)

        bin_A = RoundedRectangle(width=3, height=2, corner_radius=0.2, color=BLUE).to_edge(LEFT, buff=1.5)
        bin_B = RoundedRectangle(width=3, height=2, corner_radius=0.2, color=RED).to_edge(RIGHT, buff=1.5)
        bin_A_label = Text("Group A").next_to(bin_A, UP)
        bin_B_label = Text("Group B").next_to(bin_B, UP)

        self.play(Create(bin_A), Create(bin_B), Write(bin_A_label), Write(bin_B_label))
        self.wait(1)

        sum_A = Integer(0, color=BLUE).scale(1.5).next_to(bin_A, DOWN, buff=0.3)
        sum_B = Integer(0, color=RED).scale(1.5).next_to(bin_B, DOWN, buff=0.3)
        self.play(Write(sum_A), Write(sum_B))

        # Re-get the numbers from the VGroup for animation
        num8, num7, num6, num5 = numbers_tex
        self.play(
            num8.animate.move_to(bin_A.get_center() + LEFT*0.5),
            num5.animate.move_to(bin_A.get_center() + RIGHT*0.5),
            num7.animate.move_to(bin_B.get_center() + LEFT*0.5),
            num6.animate.move_to(bin_B.get_center() + RIGHT*0.5),
        )
        self.play(sum_A.animate.set_value(13), sum_B.animate.set_value(13))

        equals_sign = MathTex("=", color=GREEN).scale(2).move_to(ORIGIN)
        checkmark = MathTex(r"\checkmark", color=GREEN).scale(3).next_to(equals_sign, RIGHT, buff=0.5)
        
        self.play(Write(equals_sign), Write(checkmark))
        self.wait(3)

        # --- SEQUENCE 3: MAPPING TO SPINS ---

        all_partition_elements = VGroup(
            problem_title, numbers_tex, bin_A, bin_B, bin_A_label,
            bin_B_label, sum_A, sum_B, equals_sign, checkmark
        )
        self.play(FadeOut(all_partition_elements))
        self.wait(0.5)

        numbers_tex_centered = VGroup(*[MathTex(str(n)) for n in numbers_list]).arrange(RIGHT, buff=1.5).scale(1.8)
        self.play(Write(numbers_tex_centered))
        
        spins_tex = VGroup(
            MathTex("+1", color=PLUS_ONE_COLOR), MathTex("-1", color=MINUS_ONE_COLOR),
            MathTex("-1", color=MINUS_ONE_COLOR), MathTex("+1", color=PLUS_ONE_COLOR)
        ).scale(1.5)

        for i, spin in enumerate(spins_tex):
            spin.next_to(numbers_tex_centered[i], DOWN, buff=0.5)

        self.play(Write(spins_tex))
        self.wait(3)

        calc_sum = MathTex(
            r"(+1)\times 8", r"+ (-1)\times 7", r"+ (-1)\times 6", r"+ (+1)\times 5", r" = 0"
        ).scale(1.2).next_to(numbers_tex_centered, DOWN, buff=1.5)
        
        self.play(LaggedStart(*[Write(part) for part in calc_sum], lag_ratio=0.5, run_time=3))
        self.wait(3)

        goal_formula = MathTex(r"\text{Goal: Find } s_i \text{ such that } \sum_i s_i a_i = 0", font_size=48)
        goal_formula.to_edge(DOWN)
        
        self.play(ReplacementTransform(calc_sum, goal_formula))
        self.wait(3)

        # --- SEQUENCE 4: THE CONNECTION TO HAMILTONIAN ---

        all_prev_elements = VGroup(numbers_tex_centered, spins_tex)
        self.play(FadeOut(all_prev_elements), goal_formula.animate.move_to(ORIGIN))
        self.wait(1)

        squared_sum = MathTex(r"\left( \sum_i s_i a_i \right)^2", font_size=60)
        self.play(ReplacementTransform(goal_formula, squared_sum))
        self.wait(2)

        # --- FIX #2: Re-layout the long formula to prevent clipping ---
        self.play(squared_sum.animate.to_edge(UP, buff=1.0))
        
        expanded_term1 = MathTex(r"= \sum_i (a_i)^2", font_size=60)
        expanded_term2 = MathTex(r"+ \sum_{i \neq j}", r"a_i a_j", r"s_i s_j", font_size=60)
        expanded_form = VGroup(expanded_term1, expanded_term2).arrange(RIGHT, buff=0.2)
        expanded_form.next_to(squared_sum, DOWN, buff=0.5)

        self.play(Write(expanded_form))
        self.wait(2)

        const_part = expanded_form[0]
        const_label = Text("CONSTANT", color=YELLOW, font_size=32).next_to(const_part, DOWN)
        self.play(Write(const_label))
        self.wait(2)

        variable_part = expanded_form[1]
        self.play(
            FadeOut(const_part, const_label, squared_sum),
            variable_part.animate.move_to(ORIGIN).scale(0.9)
        )
        self.wait(2)
        
        hamiltonian = MathTex(r"H = \sum_{i<j}", r"J_{ij}", r"s_i s_j", font_size=60)
        hamiltonian.set_color_by_tex_to_color_map({"H": H_COLOR, "J_{ij}": J_COLOR})
        hamiltonian.next_to(variable_part, UP, buff=1.0)
        self.play(Write(hamiltonian))
        self.wait(2)

        rect1 = SurroundingRectangle(variable_part[1], color=ORANGE)
        rect2 = SurroundingRectangle(hamiltonian[1], color=ORANGE)
        
        equivalence_map = MathTex(r"J_{ij} = a_i a_j", color=YELLOW, font_size=60)
        equivalence_map.next_to(variable_part, DOWN, buff=1.0)

        self.play(Create(rect1), Create(rect2))
        self.wait(1)
        self.play(Write(equivalence_map))
        self.wait(4)

        self.play(
            FadeOut(variable_part, hamiltonian, rect1, rect2, equivalence_map)
        )
        self.wait(0.5)
        
        # --- FIX #3: Adjust box width and text size to fit properly ---
        box1 = RoundedRectangle(height=1.5, width=4.5, corner_radius=0.2, color=TEAL)
        # Reduce font size to prevent overflow
        text1 = Text("Number Partitioning", font_size=32).move_to(box1.get_center()) 
        problem1 = VGroup(box1, text1)

        box2 = RoundedRectangle(height=1.5, width=4.5, corner_radius=0.2, color=H_COLOR)
        # Reduce font size to prevent overflow
        text2 = Text("Ising Ground State", font_size=32).move_to(box2.get_center()) 
        problem2 = VGroup(box2, text2)

        problems = VGroup(problem1, problem2).arrange(RIGHT, buff=2.0)
        
        arrow = Arrow(problem1.get_right(), problem2.get_left(), buff=0.2, color=YELLOW)
        arrow_text = Text("is equivalent to").next_to(arrow, 2.7*UP)

        self.play(FadeIn(problem1))
        self.wait(1)
        self.play(GrowArrow(arrow), Write(arrow_text))
        self.wait(1)
        self.play(ReplacementTransform(problem1.copy(), problem2))
        self.wait(5)

        # --- NEW SEQUENCE: THE ROGUES' GALLERY (FINAL POLISHED VERSION) ---

        # 1. Define a consistent helper function for creating problem boxes
        def create_problem_box(text, color, height=1.3, width=4.0):
            box = RoundedRectangle(height=height, width=width, corner_radius=0.2, color=color)
            # This ensures the text always fits nicely inside the box
            label = Text(text, font_size=36).scale_to_fit_width(width * 0.85)
            label.move_to(box.get_center())
            return VGroup(box, label)

        # 2. Define the FINAL state of all objects for the smooth transition
        
        # A. The new, slightly larger central hub
        central_hub_final = create_problem_box("Ising Ground State", H_COLOR, height=1.5, width=5.2)
        central_hub_final.move_to(ORIGIN) # Place the final hub at the center

        # B. The final position and look of the Number Partitioning box
        np_box_final = create_problem_box("Number Partitioning", TEAL)
        np_box_final.move_to(central_hub_final.get_center() + DOWN * 2.2 + LEFT * 3.5)

        # C. The final arrow connecting them, based on their final positions
        np_arrow_final = Arrow(
            np_box_final.get_top(), central_hub_final.get_corner(DL),
            buff=0.2, color=YELLOW
        )

        # 3. Perform the main transition in ONE smooth animation
        # We transform the old objects (problem1, problem2, arrow) into their new final versions.
        # This handles moving, resizing, and reshaping all at once.
        self.play(
            FadeOut(arrow_text),
            Transform(problem1, np_box_final),       # The old NP box becomes the new one
            Transform(problem2, central_hub_final),  # The old Ising box becomes the new hub
            Transform(arrow, np_arrow_final),        # The old arrow becomes the new, correctly angled one
            run_time=2.0
        )
        self.wait(1)

        # 4. Sequentially introduce the other problems, now that the scene is set
        
        # Get the final objects from the Transform to use as references
        central_hub = problem2
        np_box = problem1
        
        # Max-Cut
        max_cut_box = create_problem_box("Max-Cut", PURPLE)
        max_cut_box.move_to(central_hub.get_center() + UP * 2.2 + LEFT * 3.5)
        max_cut_arrow = Arrow(max_cut_box.get_bottom(), central_hub.get_corner(UL), buff=0.2, color=YELLOW)
        self.play(FadeIn(max_cut_box))
        self.play(GrowArrow(max_cut_arrow))
        self.wait(2.5)

        # Traveling Salesman
        tsp_box = create_problem_box("Traveling Salesman", MAROON_B)
        tsp_box.move_to(central_hub.get_center() + UP * 2.2 + RIGHT * 3.5)
        tsp_arrow = Arrow(tsp_box.get_bottom(), central_hub.get_corner(UR), buff=0.2, color=YELLOW)
        self.play(FadeIn(tsp_box))
        self.play(GrowArrow(tsp_arrow))
        self.wait(2.5)

        # ksat
        ksat_box = create_problem_box("k-SAT", GOLD_D)
        ksat_box.move_to(central_hub.get_center() + DOWN * 2.2 + RIGHT * 3.5)
        ksat_arrow = Arrow(ksat_box.get_top(), central_hub.get_corner(DR), buff=0.2, color=YELLOW)
        self.play(FadeIn(ksat_box))
        self.play(GrowArrow(ksat_arrow))
        self.wait(2.5)
        
        # 5. Final shot - group everything for a clean end frame
        
        all_problems_group = VGroup(
            central_hub,
            np_box, arrow, # The NP box and its arrow are already grouped from the transform
            max_cut_box, max_cut_arrow,
            tsp_box, tsp_arrow,
            ksat_box, ksat_arrow
        )
        
        # A final small adjustment to ensure the whole composition is perfectly centered
        self.play(all_problems_group.animate.move_to(ORIGIN))
        self.wait(5)
    
        # (This code follows immediately after the final zoom-out of the problems group)

        # --- NEW SEQUENCE: THE ESSENCE OF THE ISING PROBLEM ---

        # 1. Clean up the screen
        self.play(FadeOut(all_problems_group))
        self.wait(0.5)

        # 2. Define the positions for the formula and the graph
        formula_pos = UP * 2.5
        graph_pos = DOWN * 0.5

        # 3. Create and place the Hamiltonian formula first
        hamiltonian_essence = MathTex(r"H = \sum_{i<j} J_{ij} s_i s_j", font_size=72)
        hamiltonian_essence.set_color_by_tex_to_color_map({"H": H_COLOR, "J_{ij}": J_COLOR})
        hamiltonian_essence.move_to(formula_pos)
        
        self.play(Write(hamiltonian_essence))
        self.wait(2)

        # 4. Create a generic, complex-looking graph below the formula
        num_nodes = 20
        nodes = VGroup(*[
            Dot(color=WHITE) for _ in range(num_nodes)
        ])
        # Arrange in a grid with some randomness
        nodes.arrange_in_grid(4, 5, buff=1.2).scale(0.7)
        nodes.rotate(PI/6)
        for node in nodes:
            node.shift(
                (random.random() - 0.5) * 0.4 * RIGHT + 
                (random.random() - 0.5) * 0.4 * UP
            )

        lines = VGroup()
        # Use itertools.combinations to avoid duplicate edges and self-loops
        all_possible_pairs = list(itertools.combinations(range(num_nodes), 2))
        # Select a random subset of these pairs to form the edges
        num_edges = int(num_nodes * 1.5) # A reasonable number of edges
        selected_pairs = random.sample(all_possible_pairs, num_edges)
        for pair in selected_pairs:
            lines.add(Line(nodes[pair[0]].get_center(), nodes[pair[1]].get_center(), stroke_width=2, color=GRAY, z_index=-1))
        
        graph_system = VGroup(lines, nodes).move_to(graph_pos)

        self.play(Create(graph_system))
        self.wait(2)

        # 5. Animate the "flickering" search for the ground state
        flicker_duration = 0.15 # Slightly faster flicker
        for _ in range(12): # Flicker a bit more
            new_colors = [random.choice([PLUS_ONE_COLOR, MINUS_ONE_COLOR]) for _ in range(num_nodes)]
            self.play(
                *[nodes[i].animate.set_color(new_colors[i]) for i in range(num_nodes)],
                run_time=flicker_duration
            )
        
        # Settle into a final state
        final_colors = [random.choice([PLUS_ONE_COLOR, MINUS_ONE_COLOR]) for _ in range(num_nodes)]
        self.play(
            *[nodes[i].animate.set_color(final_colors[i]) for i in range(num_nodes)],
            run_time=0.5
        )

        # Highlight the minimized Hamiltonian
        self.play(Indicate(hamiltonian_essence, color=H_COLOR, scale_factor=1.1))
        self.wait(3)

        # 6. Pose the final question as a hook
        self.play(FadeOut(graph_system), FadeOut(hamiltonian_essence))
        self.wait(0.5)

        final_question = MarkupText(
            'But if brute force is impossible... <span color="YELLOW">how do we find it?</span>',
            font_size=42,
            justify=True
        ).move_to(ORIGIN) # Center the question
        
        self.play(Write(final_question))
        self.wait(5)
    
        # (This code follows immediately after the final question "how do we find it?")

        # --- NEW SEQUENCE: THE EDGE OF SOLVABILITY ---

        # 1. Answer the question with nuance (with text wrapping)
        # Relies on Manim's default center alignment for MarkupText with newlines.
        answer_text = MarkupText(
            'The short answer: for a general, complex system...\n<span color="YELLOW">you don\'t.</span>',
            font_size=42
        )
        self.play(ReplacementTransform(final_question, answer_text))
        self.wait(3)

        explanation_text = MarkupText(
            'There is no known algorithm that can efficiently find the <span color="YELLOW">exact</span>\nground state for any arbitrary set of tensions.',
            font_size=36
        ).move_to(ORIGIN)
        
        self.play(ReplacementTransform(answer_text, explanation_text))
        self.wait(4)
        self.play(FadeOut(explanation_text))
        self.wait(0.5)
        
        # 2. Show the "Rare Exact Solutions"
        title = Text("Rare Exact Solutions", font_size=42).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # A) 2D Planar Graph (Onsager's Solution)
        planar_label = Text("2D Planar Graphs", font_size=32).next_to(title, DOWN, buff=0.5)
        
        grid = VGroup(*[Dot() for i in range(25)]).arrange_in_grid(5, 5, buff=0.8)
        lines = VGroup()
        for i in range(5):
            for j in range(4):
                lines.add(Line(grid[i*5+j], grid[i*5+j+1], stroke_width=2, color=GRAY))
        for i in range(4):
            for j in range(5):
                lines.add(Line(grid[i*5+j], grid[(i+1)*5+j], stroke_width=2, color=GRAY))

        planar_system = VGroup(grid, lines).scale(0.8).next_to(planar_label, DOWN, buff=0.8)
        
        onsager_text = VGroup(
            Text("Lars Onsager", font_size=36),
            Text("1944", font_size=32, color=YELLOW)
        ).arrange(DOWN).next_to(planar_system, RIGHT, buff=0.5)

        planar_group = VGroup(planar_label, planar_system, onsager_text)
        self.play(Write(planar_group))
        self.wait(5)
        
        # B) Spin Glass / Parisi case
        spinglass_label = Text("Spin Glasses (Random Tensions)", font_size=32).next_to(title, DOWN, buff=0.5)
        
        num_nodes = 15
        nodes = VGroup(*[Dot() for _ in range(num_nodes)]).arrange_in_grid(3, 5, buff=1.5)
        for node in nodes:
            node.shift((random.random()-0.5)*0.5*RIGHT + (random.random()-0.5)*0.5*UP)
        
        lines = VGroup()
        all_pairs = list(itertools.combinations(range(num_nodes), 2))
        selected_pairs = random.sample(all_pairs, int(num_nodes * 1.8))
        for pair in selected_pairs:
            color = random.choice([PLUS_ONE_COLOR, MINUS_ONE_COLOR])
            lines.add(Line(nodes[pair[0]], nodes[pair[1]], color=color, stroke_width=2, z_index=-1))
            
        spinglass_system = VGroup(nodes, lines).scale(0.7).next_to(spinglass_label, DOWN, buff=0.5)
        
        parisi_text = VGroup(
            Text("Giorgio Parisi", font_size=36),
            MarkupText("Statistical Properties", font_size=28),
            Text("Nobel Prize 2021", font_size=32, color=YELLOW)
        ).arrange(DOWN, buff=0.2).next_to(spinglass_system, RIGHT, buff=0.5)

        spinglass_group = VGroup(spinglass_label, spinglass_system, parisi_text)
        self.play(ReplacementTransform(planar_group, spinglass_group))
        self.wait(5)

        # 3. Transition to Quantum Annealing
        self.play(FadeOut(title), FadeOut(spinglass_group))
        self.wait(0.5)

        outro_text = MarkupText(
            "For the messy, real-world problems,\nwe need a different approach...",
            font_size=36
        ).move_to(UP * 2.5)

        self.play(Write(outro_text))
        self.wait(3)

        # 4. Show the D-Wave Computer
        try:
            dwave_image = ImageMobject("dwave_computer.jpeg")
            dwave_image.set_height(4.5)
            dwave_image.next_to(outro_text, DOWN, buff=0.5)
            
            self.play(FadeIn(dwave_image))
            
            dwave_label = Text("Quantum Annealer", font_size=42, color=TEAL)
            dwave_label.next_to(dwave_image, DOWN)
            self.play(Write(dwave_label))
            self.wait(5)
            
        except FileNotFoundError:
            self.play(Write(Text("Image 'dwave_computer.jpeg' not found.", color=RED)))
            self.wait(3)


def calculate_min_H(J):
    N = len(J)
    # Generate all 2^(N-1) combinations for the first N-1 spins
    # The last spin is fixed to -1 to break the s -> -s symmetry
    # This is okay because we only care about the structure of one of the two ground states.
    num_combos = 2**(N - 1)
    # Using a direct array approach to build combinations
    # This is more memory-intensive but conceptually clear for smaller N
    combos = np.ones((num_combos, N), dtype=int)
    for i in range(N - 1):
        n = 2**(N - 1 - (i + 1))
        combos[:, i] = np.tile(np.repeat(np.array([1, -1]), n), 2**i)
    combos[:, -1] = -1

    # Einsum is a very efficient way to compute the Hamiltonian for all combos at once
    # H_i = s_i^T . J . s_i
    H = 0.5 * np.einsum('ij,jk,ik->i', combos, J, combos)
    min_H_index = np.argmin(H)
    return np.min(H), combos[min_H_index]
def J_order(N, d):
    def f(i, j):
        return ((i+1)/N)**d + ((j+1)/N)**d
    mat = np.fromfunction(f, (N, N), dtype=float)
    np.fill_diagonal(mat, 0)
    return mat


class OrderedJ(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        PLUS_ONE_COLOR = BLUE_D
        MINUS_ONE_COLOR = RED_D
        J_COLOR = YELLOW
        H_COLOR = GREEN
        
        # --- SEQUENCE 1: THE SPARK OF AN IDEA ---

        # 1. Opening text about J_ij
        title_text = Text("The Ising model is defined by its matrix of tensions,", font_size=36)
        hamiltonian_formula = MathTex(r"H = \sum_{i<j} J_{ij} s_i s_j", font_size=48).next_to(title_text, DOWN, buff=0.4)
        hamiltonian_formula.set_color_by_tex("J_{ij}", J_COLOR)
        
        opening_group = VGroup(title_text, hamiltonian_formula).move_to(ORIGIN)
        
        self.play(Write(opening_group))
        self.play(Indicate(hamiltonian_formula.get_part_by_tex("J_{ij}"), scale_factor=1.2, color=J_COLOR))
        self.wait(3)
        self.play(FadeOut(opening_group))
        self.wait(0.5)

        # 2. Pose the student's question
        question = Text("A young physics student wondered...", font_size=36).to_edge(2*UP)
        sub_question = Text(
            "What if the interaction was not random,\nbut based on a simple, underlying rule?",
            font_size=32, line_spacing=1.2
        ).move_to(ORIGIN)

        self.play(Write(question))
        self.play(Write(sub_question))
        self.wait(3)
        self.play(FadeOut(question, sub_question))
        self.wait(0.5)
        
        # --- SEQUENCE 2: THE WALL OF EVIDENCE (d=1) ---

        # 1. Show the simple rule
        rule_formula = MathTex("J_{ij} = i + j", font_size=48)
        rule_formula.to_edge(UP, buff=1.0)
        self.play(Write(rule_formula))
        self.wait(2)

        # 2. Pre-calculate ground states for d=1
        ground_states = {}
        for n in range(10, 16):
            j_matrix = J_order(n, d=1)
            _, s_g = calculate_min_H(j_matrix)
            ground_states[n] = s_g

        # 3. Animate the "Wall of Evidence"
        dot_rows = VGroup()
        for n in range(10, 16):
            # Create the label and the row of dots
            n_label = MathTex(f"N={n}", font_size=32)
            dot_row = VGroup(*[Dot(radius=0.1, color=WHITE) for _ in range(n)]).arrange(RIGHT, buff=0.25)
            
            row_group = VGroup(n_label, dot_row).arrange(RIGHT, buff=0.5)
            dot_rows.add(row_group)

        dot_rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(ORIGIN)

        # Animate each row appearing and resolving
        for i, n in enumerate(range(10, 16)):
            self.play(FadeIn(dot_rows[i]), run_time=0.5)
            self.wait(0.5)
            
            s_g = ground_states[n]
            animations = []
            for j, spin in enumerate(s_g):
                color = PLUS_ONE_COLOR if spin == 1 else MINUS_ONE_COLOR
                animations.append(dot_rows[i][1][j].animate.set_color(color))
            
            self.play(LaggedStart(*animations, lag_ratio=0.1))
            self.wait(1)

        self.wait(3)


        # --- SEQUENCE 3: GENERALIZING TO 'd' ---

        # 1. Morph the formula to the general case
        general_rule = MathTex(r"J_{ij} \propto i^d + j^d", font_size=48).move_to(rule_formula)
        general_rule.set_color_by_tex("d", ORANGE)
        self.play(Transform(rule_formula, general_rule))
        self.wait(2)

        # 2. Set up the interactive demonstration
        # Make the "wall of evidence" fully opaque again for the main demonstration
        self.play(dot_rows.animate.fade(0))

        # Create the dial for 'd' below the rows
        d_dial = NumberLine(
            x_range=[-8, 8, 2], # Adjusted for better visual spacing of ticks
            length=10,
            include_numbers=True,
            label_direction=UP
        ).next_to(dot_rows, DOWN, buff=0.8)
        d_label = MathTex("d", color=ORANGE).next_to(d_dial, DOWN)
        
        self.play(Create(d_dial), Write(d_label))
        self.wait(1)

        # 3. Pre-calculate the TRUE ground states for different 'd' for ALL Ns
        def get_M(n, d):
            j_mat = J_order(n, d)
            _, s_g = calculate_min_H(j_mat)
            return np.sum(s_g == 1)

        M_values = {}
        d_points = [-2.0, 4.0, 6.0] # The points we will visit, d=1 is already shown
        all_n_values = range(10, 16)

        for d_val in d_points:
            M_values[d_val] = {}
            for n_val in all_n_values:
                M_values[d_val][n_val] = get_M(n_val, d_val)

        # 4. Animate the pointer and ALL state changes simultaneously
        pointer = Arrow(start=d_dial.n2p(1) + UP*0.5, end=d_dial.n2p(1), color=ORANGE, buff=0)
        self.play(GrowArrow(pointer))
        self.wait(1)

        # Helper function to generate the list of animations for any 'd'
        def get_update_animations(d_val):
            anims = []
            for i, n in enumerate(all_n_values):
                M = M_values[d_val][n]
                # Get the dot VGroup for the current row
                current_dots = dot_rows[i][1]
                for j in range(n):
                    color = PLUS_ONE_COLOR if j < M else MINUS_ONE_COLOR
                    anims.append(current_dots[j].animate.set_color(color))
            return anims

        # Animate to d=6
        self.play(
            pointer.animate.move_to(d_dial.n2p(6) + UP*0.25),
            LaggedStart(*get_update_animations(6.0), lag_ratio=0.01),
            run_time=2.5
        )
        self.wait(1)
        
        # Animate to d=4.0
        self.play(
            pointer.animate.move_to(d_dial.n2p(4) + UP*0.25),
            LaggedStart(*get_update_animations(4.0), lag_ratio=0.01),
            run_time=3.0
        )
        self.wait(1)

        # Animate to d=-2
        self.play(
            pointer.animate.move_to(d_dial.n2p(-2) + UP*0.25),
            LaggedStart(*get_update_animations(-2.0), lag_ratio=0.01),
            run_time=2.0
        )
        self.wait(2)


class ConvergingRatio(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        PLUS_ONE_COLOR = BLUE_D
        MINUS_ONE_COLOR = RED_D
        J_COLOR = YELLOW
        D_COLOR = ORANGE
        Q_COLOR = YELLOW

        # Helper function for this scene
        def calculate_min_J_o(J):
            N = len(J)
            H_l = []
            for M in range(N + 1):
                s = np.array([1]*M + [-1]*(N - M), dtype=float)
                H = 0.5 * s @ J @ s
                H_l.append(H)
            
            min_H_idx = np.argmin(H_l)
            return min_H_idx

        # --- SEQUENCE 1: DEFINING THE RATIO q ---

        N_rep, d_rep = 12, 1
        j_mat_rep = J_order(N_rep, d_rep)
        M_rep = calculate_min_J_o(j_mat_rep)

        s_vector = VGroup(*[
            Dot(radius=0.15, color=PLUS_ONE_COLOR if i < M_rep else MINUS_ONE_COLOR)
            for i in range(N_rep)
        ]).arrange(RIGHT, buff=0.3)
        
        self.play(Write(s_vector))
        self.wait(2)

        brace = Brace(s_vector[:M_rep], direction=UP, color=WHITE)
        m_label = brace.get_text("M")
        m_label.set_color(Q_COLOR).scale(1.2)
        
        self.play(GrowFromCenter(brace), Write(m_label))
        self.wait(2)

        q_formula = MathTex("q", "=", "{M", r"\over", "N}").set_color_by_tex("q", Q_COLOR)
        q_formula.next_to(s_vector, DOWN, buff=0.8)
        q_formula.get_part_by_tex("M").set_color(Q_COLOR)
        
        self.play(Write(q_formula))
        self.wait(3)

        # --- SEQUENCE 2: THE CONVERGENCE GRAPH ---
        
        self.play(FadeOut(s_vector, brace, m_label, q_formula))
        self.wait(0.5)

        ax = Axes(
            x_range=[0, 105, 10], y_range=[0, 1, 0.1],
            x_length=10, y_length=5.5, # y_length is slightly smaller
            axis_config={"color": BLUE},
            y_axis_config={"decimal_number_config": {"num_decimal_places": 1}}
        )
        x_label = ax.get_x_axis_label("N \\text{ (Number of Spins)}")
        y_label = ax.get_y_axis_label("q = M/N", direction=UP).shift(LEFT*0.5)
        
        # Corrected: Scale and shift the entire graph down
        graph = VGroup(ax, x_label, y_label).scale(0.9).shift(DOWN * 0.5)

        self.play(Create(graph))
        self.wait(1)

        max_N_brute = 30
        max_N_total = 100
        d_values = [1.0, -0.5, 4]
        q_data = {d: [] for d in d_values}
        
        for d in d_values:
            for n in range(2, max_N_total + 1):
                j_mat = J_order(n, d)
                M = calculate_min_J_o(j_mat)
                q_data[d].append(M / n if n > 0 else 0)

        d1_color = GREEN
        d1_label = MathTex("d=1", color=d1_color).next_to(ax.c2p(max_N_total, q_data[1.0][-1]), RIGHT)
        self.play(Write(d1_label))

        d1_dots_brute = VGroup(*[
            Dot(ax.c2p(n, q_data[1.0][n-2]), color=d1_color, radius=0.05)
            for n in range(2, max_N_brute + 1)
        ])
        
        self.play(LaggedStart(*[Create(d) for d in d1_dots_brute], lag_ratio=0.1, run_time=3))
        self.wait(1)

        wall = DashedLine(ax.c2p(max_N_brute, 0), ax.c2p(max_N_brute, 1), color=RED)
        wall_label = Text("Brute-Force Wall", font_size=24, color=RED)
        wall_label.next_to(wall.get_top(), UP, buff=0.1)
        
        self.play(Create(wall), Write(wall_label))
        self.wait(2)
        
        # This text will now fit comfortably
        leap_of_faith_text = Text(
            "Assume the two-cluster pattern always holds.",
            font_size=30, color=YELLOW
        ).to_edge(UP)
        self.play(Write(leap_of_faith_text))
        self.wait(2)

        complexity_before = MathTex("2^N", r"\gg", "N").scale(1.5).next_to(leap_of_faith_text, DOWN, buff=0.5).to_edge(RIGHT, buff=1.5)
        complexity_after = MathTex("N").scale(1.5).move_to(complexity_before)
        
        self.play(Write(complexity_before))
        self.wait(1)
        self.play(Transform(complexity_before, complexity_after), FadeOut(leap_of_faith_text))
        self.play(FadeOut(complexity_before))
        self.wait(0.5)

        d1_dots_assumed = VGroup(*[
            Dot(ax.c2p(n, q_data[1.0][n-2]), color=d1_color, radius=0.05)
            for n in range(max_N_brute + 1, max_N_total + 1)
        ])
        self.play(Create(d1_dots_assumed), run_time=1)
        self.wait(1)

        d_colors = {-0.5: PINK, 4: PURPLE}
        for d in [-0.5, 4]:
            label = MathTex(f"d={d}", color=d_colors[d]).next_to(ax.c2p(max_N_total, q_data[d][-1]), RIGHT)
            dots = VGroup(*[Dot(ax.c2p(n, q_data[d][n-2]), color=d_colors[d], radius=0.05) for n in range(2, max_N_total + 1)])
            self.play(Write(label), Create(dots), run_time=1.5)

        self.wait(5)


class GroundStateCalculation(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        PLUS_ONE_COLOR = BLUE_D
        MINUS_ONE_COLOR = RED_D
        J_COLOR = YELLOW
        D_COLOR = ORANGE
        PINK_TERM_COLOR = PINK
        H_COLOR = GREEN
        # --- SEQUENCE 1: FORMALIZING THE INTERACTION MATRIX ---
        
        recap_text = Text(
            "So, having seen the ratio 'q' converge for any given 'd'...",
            font_size=36
        ).to_edge(UP)
        proportional_formula = MathTex(r"J_{ij} \propto i^d + j^d", font_size=60)
        proportional_formula.set_color_by_tex("d", D_COLOR)
        proportional_formula.next_to(recap_text, DOWN, buff=0.5)
        self.play(Write(recap_text))
        self.play(Write(proportional_formula))
        self.wait(3)
        formalization_text = MathTex(
            r"\text{...he formalized this idea, naming the interaction matrix } J^{(N, d)},",
            font_size=38
        )
        formalization_text.set_color_by_tex("J^{(N, d)}", J_COLOR)
        formalization_text.next_to(proportional_formula, DOWN, buff=0.8)
        formalization_text_2 = Text(
            "adding some terms for convenience and rigor.",
            font_size=32
        ).next_to(formalization_text, DOWN)
        self.play(Write(formalization_text), Write(formalization_text_2))
        self.wait(3)

        # --- THIS IS THE FIX ---
        # Build the formula in parts to reference the Kronecker delta term reliably
        part1 = MathTex(r"J_{ij}^{(N, d)}", r"=", r"\frac{1}{N^d}", r"(i^d + j^d)")
        part2 = MathTex(r"(1 - \delta_{ij})") # This is the part we want to reference
        
        # Color the parts
        part1.set_color_by_tex_to_color_map({
            "J_{ij}^{(N, d)}": J_COLOR, "N": WHITE, "d": D_COLOR, "i": BLUE, "j": GREEN
        })
        part2.set_color_by_tex(r"\delta_{ij}", PINK_TERM_COLOR)

        # Group and arrange them
        formal_formula_group = VGroup(part1, part2).arrange(RIGHT, buff=0.2)
        formal_formula_group.move_to(proportional_formula)

        self.play(
            FadeOut(recap_text, formalization_text, formalization_text_2),
            Transform(proportional_formula, formal_formula_group)
        )
        formula = proportional_formula # Keep the handle
        self.wait(2)
        
        # Now, we can reliably reference part2
        kronecker_term_part = formula.submobjects[1] # part2 is the second element of the VGroup
        kronecker_explanation = Text(
            "(This just means the diagonals are zero)",
            font_size=24, color=GRAY
        ).next_to(kronecker_term_part, DOWN, buff=0.3)
        
        self.play(Indicate(kronecker_term_part, color=PINK_TERM_COLOR), Write(kronecker_explanation))
        self.wait(3)
        self.play(FadeOut(kronecker_explanation))

        # 4. Show the concrete example for N=5, d=2
        example_label = MathTex("N=5, d=2", font_size=42).set_color_by_tex("d", D_COLOR)
        matrix_values = [
            [0, 5, 10, 17, 26], [5, 0, 13, 20, 29], [10, 13, 0, 25, 34],
            [17, 20, 25, 0, 41], [26, 29, 34, 41, 0]
        ]
        j52_lhs = MathTex(r"J^{(5, 2)}", "=", r"\frac{1}{5^2}").set_color_by_tex("J", J_COLOR)
        j52_matrix = IntegerMatrix(matrix_values, h_buff=0.8)
        
        example_matrix_group = VGroup(j52_lhs, j52_matrix).arrange(RIGHT, buff=0.3)
        full_example = VGroup(example_label, example_matrix_group).arrange(DOWN, buff=0.4)
        full_example.next_to(formula, DOWN, buff=0.5).scale(0.8)

        self.play(Write(example_label))
        self.play(Write(j52_lhs), Create(j52_matrix))
        self.wait(5)

        # --- SEQUENCE 2: POSTULATING THE GROUND STATE ---

        self.play(FadeOut(full_example), formula.animate.to_edge(UP, buff=1.0))
        self.wait(0.5)

        postulate_text = Text(
            "...with the postulated ground state of the following form:",
            font_size=36
        ).next_to(formula, DOWN, buff=0.7)
        self.play(Write(postulate_text))
        self.wait(2)

        # 3. Display the ground state vector s_g^T as specified
        s_g_label = MathTex(r"\pmb{s}_g^T", r"=", font_size=60)
        
        up_spin = MathTex("+1", color=PLUS_ONE_COLOR)
        down_spin = MathTex("-1", color=MINUS_ONE_COLOR)
        dots = MathTex(r"\dots").scale(1.2)

        # Using your specified layout for a clearer "block" visual
        spin_vector_content = VGroup(
            up_spin,
            up_spin.copy(),
            dots.copy(),
            up_spin.copy(),
            dots.copy(),
            down_spin.copy(),
            down_spin.copy(),
            dots.copy(),
            down_spin
        ).arrange(RIGHT, buff=0.3) # Slightly reduced buff for a denser look

        bracket_l = MathTex(r"\big[", font_size=120).next_to(spin_vector_content, LEFT, buff=0.2)
        bracket_r = MathTex(r"\big]", font_size=120).next_to(spin_vector_content, RIGHT, buff=0.2)
        
        s_g_vector = VGroup(bracket_l, spin_vector_content, bracket_r)
        
        full_s_g_display = VGroup(s_g_label, s_g_vector).arrange(RIGHT, buff=0.4)
        full_s_g_display.next_to(postulate_text, DOWN, buff=0.7)

        self.play(Write(full_s_g_display))
        self.wait(2)

        # 4. Add the brace for M underneath the first cluster
        # The first cluster consists of the first 4 elements in spin_vector_content
        first_cluster = spin_vector_content[:4]
        
        m_brace = Brace(first_cluster, direction=DOWN, color=WHITE)
        m_label = m_brace.get_text("M spins")
        
        self.play(
            GrowFromCenter(m_brace),
            Write(m_label)
        )
        self.wait(4)

        # --- SEQUENCE 3: Z2 SYMMETRY AND CONVENTION (ROBUST VERSION) ---

        # 1. Show the compact Hamiltonian
        hamiltonian_compact = MathTex("H", "=", r"\frac{1}{2}", r"\pmb{s}^T", "J", r"\pmb{s}", font_size=48)
        hamiltonian_compact.next_to(full_s_g_display, DOWN, buff=1.0)
        hamiltonian_compact[0].set_color(H_COLOR)
        hamiltonian_compact[4].set_color(J_COLOR)
        self.play(Write(hamiltonian_compact))
        self.wait(2)

        # --- THE FOOLPROOF FIX ---
        # Create BOTH the original and flipped targets right now.
        
        # Target 1: The original "+1 first" state
        original_spins_target = spin_vector_content.copy()

        # Target 2: The flipped "-1 first" state
        flipped_spins_target = spin_vector_content.copy()
        for elem in flipped_spins_target:
            if isinstance(elem, MathTex) and elem.get_tex_string() != r"\dots":
                if elem.get_tex_string() == "+1":
                    elem.become(MathTex("-1", color=MINUS_ONE_COLOR).move_to(elem))
                else:
                    elem.become(MathTex("+1", color=PLUS_ONE_COLOR).move_to(elem))
        
        # Create the flipped formula target
        hamiltonian_flipped = MathTex("H", "=", r"\frac{1}{2}", r"(-\pmb{s})^T", "J", r"(-\pmb{s})", font_size=48).move_to(hamiltonian_compact)
        hamiltonian_flipped[0].set_color(H_COLOR)
        hamiltonian_flipped[4].set_color(J_COLOR)

        # 2. Animate the FIRST flip
        # The on-screen 'spin_vector_content' becomes the flipped target.
        self.play(
            spin_vector_content.animate.become(flipped_spins_target),
            hamiltonian_compact.animate.become(hamiltonian_flipped),
            run_time=2.0
        )
        self.wait(3)

        # 3. State the convention and flip BACK
        self.play(FadeOut(hamiltonian_compact, m_brace, m_label))
        convention_text = Text(
            "In his notation, he chose the first cluster to be up (+1).",
            font_size=32, color=YELLOW
        ).next_to(full_s_g_display, DOWN, buff=0.8)
        self.play(Write(convention_text))
        self.wait(1)

        # Animate the on-screen vector becoming the original target.
        self.play(
            spin_vector_content.animate.become(original_spins_target),
            run_time=1.5
        )
        self.wait(5)

        # 4. ONE. FINAL. FUCKING. FLIP.
        # Animate the on-screen vector becoming the flipped target again.
        self.play(
            spin_vector_content.animate.become(flipped_spins_target),
            run_time=2.0
        )
        self.wait(5)