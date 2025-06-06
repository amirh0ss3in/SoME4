from manim import *
import random
import itertools

# Scene 1: Visualizing the Fully Connected Ising Model (Improved Self-Interaction Loops)
class FullyConnectedIsingModelN5(Scene):
    def construct(self):
        N = 5
        graph_radius = 2.3
        node_radius = 0.3
        arrow_total_length = node_radius * 0.8
        arrow_half_length = arrow_total_length / 2.0

        UP_ARROW_COLOR = BLUE_C
        DOWN_ARROW_COLOR = RED_C
        UP_CIRCLE_COLOR = BLUE_E
        DOWN_CIRCLE_COLOR = RED_E
        TRANSITION_CIRCLE_COLOR = GOLD_D
        INDEX_LABEL_COLOR = WHITE 
        EDGE_LINE_COLOR = GREY_A
        J_IJ_LABEL_COLOR = YELLOW_D 
        J_II_LABEL_COLOR = YELLOW_D 
        J_II_LOOP_COLOR = GREEN_B   

        title = Text(f"Fully Connected Ising Model (N={N})", font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(0.5)

        all_node_visuals = VGroup() 
        node_spin_directions_vectors = []
        arrow_mobjects = [] 

        for k in range(N):
            angle = TAU * k / N + PI / 2
            center_point_relative = np.array([
                graph_radius * np.cos(angle), graph_radius * np.sin(angle), 0
            ])
            spin_direction_vector = random.choice([UP, DOWN])
            node_spin_directions_vectors.append(spin_direction_vector)
            current_arrow_color = UP_ARROW_COLOR if np.array_equal(spin_direction_vector, UP) else DOWN_ARROW_COLOR
            current_circle_color = UP_CIRCLE_COLOR if np.array_equal(spin_direction_vector, UP) else DOWN_CIRCLE_COLOR
            circle = Circle(radius=node_radius, color=current_circle_color, fill_opacity=0.7, z_index=1)
            circle.move_to(center_point_relative)
            arrow = Arrow(
                start=center_point_relative - spin_direction_vector * arrow_half_length,
                end=center_point_relative + spin_direction_vector * arrow_half_length,
                buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.35, color=current_arrow_color, z_index=2
            )
            arrow_mobjects.append(arrow)
            index_label = MathTex(str(k + 1), color=INDEX_LABEL_COLOR, font_size=24, z_index=3)
            norm_center_point_relative = np.linalg.norm(center_point_relative)
            direction_to_label = (center_point_relative / norm_center_point_relative) if norm_center_point_relative > 1e-6 else UP
            label_offset_distance = node_radius + 0.3 # Clearance for index label
            index_label.move_to(center_point_relative + direction_to_label * label_offset_distance)
            all_node_visuals.add(VGroup(circle, index_label))
        
        graph_group = VGroup(all_node_visuals, *arrow_mobjects)
        graph_group.move_to(DOWN * 0.35)

        node_creation_anims = []
        for i in range(N):
            node_vis = all_node_visuals[i]
            node_creation_anims.extend([
                GrowFromCenter(node_vis[0]), Write(node_vis[1]), Create(arrow_mobjects[i])])
        self.play(LaggedStart(*node_creation_anims, lag_ratio=0.1, run_time=2.5)); self.wait(0.5)

        final_node_centers = [node_vis[0].get_center() for node_vis in all_node_visuals]
        edges_and_labels_group = VGroup()
        connecting_text = Text("Drawing connections J_ij...", font_size=24).to_edge(DOWN, buff=0.2)
        self.play(Write(connecting_text))
        half_gap_size = 0.35 
        for i in range(N):
            for j in range(i + 1, N):
                p1, p2 = final_node_centers[i], final_node_centers[j]
                label_text_obj = MathTex(f"J_{{{i+1},{j+1}}}", color=J_IJ_LABEL_COLOR, font_size=20, z_index=1)
                direction_vector = p2 - p1
                line_length = np.linalg.norm(direction_vector)
                unit_direction_vector = direction_vector / line_length if line_length > 1e-6 else RIGHT
                label_text_obj.move_to((p1 + p2) / 2)
                line_angle = angle_of_vector(direction_vector)
                label_text_obj.rotate(line_angle + (PI if PI/2 < line_angle <= 3*PI/2 else 0))
                p_before_label = (p1 + p2) / 2 - unit_direction_vector * half_gap_size
                p_after_label = (p1 + p2) / 2 + unit_direction_vector * half_gap_size
                line_segment1 = Line(p1, p_before_label, color=EDGE_LINE_COLOR, stroke_width=2.5, z_index=0) if np.linalg.norm(p_before_label - p1) > 0.05 else None
                line_segment2 = Line(p_after_label, p2, color=EDGE_LINE_COLOR, stroke_width=2.5, z_index=0) if np.linalg.norm(p2 - p_after_label) > 0.05 else None
                current_edge_elements = VGroup(label_text_obj, *filter(None, [line_segment1, line_segment2]))
                edges_and_labels_group.add(current_edge_elements)
                anim_ops = [Create(seg) for seg in filter(None, [line_segment1, line_segment2])]
                anim_ops.append(Write(label_text_obj))
                self.play(*anim_ops, run_time=0.25) # Consolidated runtime for each edge creation
        self.play(FadeOut(connecting_text)); self.wait(0.5)

        symmetry_text = MathTex(r"J_{ij} = J_{ji}", r"\text{ (symmetric couplings)}", font_size=28)
        self_interaction_text = MathTex(r"\text{No self-interactions: } J_{ii} = 0", font_size=28)
        explanatory_texts_group = VGroup(self_interaction_text, symmetry_text).arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.20)
        self.play(Write(explanatory_texts_group)); self.wait(2)

        # --- 5. No Self-Interactions (J_ii = 0) - Visual Cue ---
        self_loops_and_labels_group = VGroup()

        for k in range(N):
            node_circle = all_node_visuals[k][0]
            # node_index_mob = all_node_visuals[k][1] # We'll use its position for clearance
            node_center = node_circle.get_center()

            vec_graph_center_to_node = node_center - graph_group.get_center()
            norm_vec = np.linalg.norm(vec_graph_center_to_node)
            dir_outward = (vec_graph_center_to_node / norm_vec) if norm_vec > 1e-6 else UP
            
            loop_radius = node_radius * 0.65  # Loop is a bit smaller than the node
            arc_angle_span = TAU * 0.75      # A 'C' shape (270 degrees)
            
            # Create Arc at ORIGIN, with opening along its positive local x-axis
            # For a C opening to the right: start_angle = -arc_angle_span / 2
            self_loop = Arc(
                radius=loop_radius,
                start_angle = -arc_angle_span / 2 , # Rotate pre-creation to make opening point left
                angle=arc_angle_span,
                color=J_II_LOOP_COLOR, stroke_width=2.0, z_index=1
            )

            # Determine position for the loop's geometric center (its VGroup center)
            # It should be outside the node and the node's index label
            # Distance from node_center to place the loop's geometric center
            # Needs to clear the node (radius) and the index label (approx node_radius + 0.3 from center)
            # and then position the loop itself (whose radius is loop_radius)
            clearance_from_node_center = node_radius + 0.3 + loop_radius * 0.7 # node + index_label_space + loop_body_space
            target_loop_center_pos = node_center + dir_outward * clearance_from_node_center
            
            self_loop.move_to(target_loop_center_pos)

            
            # Rotate the loop so its opening faces somewhat tangentially or away from graph center
            # The pre-rotation by PI made it open left. Now rotate it based on dir_outward.
            # We want the "back" of the C to be towards the node.
            # The angle of dir_outward is where we want the "center" of the arc's back to point.
            # Since it was created opening left (PI radians from opening right), we rotate it by angle_of_vector(dir_outward)
            self_loop.rotate(angle_of_vector(dir_outward), about_point=self_loop.get_center())


            loop_label = MathTex(f"J_{{{k+1},{k+1}}}", color=J_II_LABEL_COLOR, font_size=18, z_index=2)
            # Position label near the loop, generally in the dir_outward direction from the loop
            loop_label.next_to(self_loop, dir_outward, buff=SMALL_BUFF * 0.7)
            
            self_loops_and_labels_group.add(VGroup(self_loop, loop_label))

        self.play(LaggedStart(*[
            AnimationGroup(Create(vg[0]), Write(vg[1])) for vg in self_loops_and_labels_group
        ], lag_ratio=0.15, run_time=1.5))
        self.wait(2)
        self.play(FadeOut(self_loops_and_labels_group, lag_ratio=0.1, run_time=1.0)); self.wait(0.5)

        self.play(FadeOut(edges_and_labels_group), FadeOut(explanatory_texts_group), run_time=1.0); self.wait(0.5)

        spin_flip_subtitle = Text("Spins can be UP or DOWN...", font_size=28).next_to(title, DOWN, buff=0.3)
        self.play(Write(spin_flip_subtitle)); self.wait(1.2) 
        num_flip_rounds = 5; nodes_indices = list(range(N))
        for i_round in range(num_flip_rounds):
            round_flip_animations, pending_updates = [], []
            num_nodes_to_flip_this_round = random.randint(1,2)
            nodes_to_flip_this_round_indices = random.sample(nodes_indices, num_nodes_to_flip_this_round)
            for node_idx in nodes_to_flip_this_round_indices:
                current_circle, old_arrow = all_node_visuals[node_idx][0], arrow_mobjects[node_idx]
                node_circle_center = current_circle.get_center()
                new_spin_direction = DOWN if np.array_equal(node_spin_directions_vectors[node_idx],UP) else UP
                new_arrow_color = UP_ARROW_COLOR if np.array_equal(new_spin_direction,UP) else DOWN_ARROW_COLOR
                new_stable_circle_color = UP_CIRCLE_COLOR if np.array_equal(new_spin_direction,UP) else DOWN_CIRCLE_COLOR
                new_arrow = Arrow(start=node_circle_center-new_spin_direction*arrow_half_length,
                                  end=node_circle_center+new_spin_direction*arrow_half_length,
                                  buff=0,stroke_width=6,max_tip_length_to_length_ratio=0.35,color=new_arrow_color,z_index=2)
                flip_sequence = Succession(ApplyMethod(current_circle.set_color,TRANSITION_CIRCLE_COLOR,run_time=0.3),
                                           ReplacementTransform(old_arrow,new_arrow,run_time=0.7),
                                           ApplyMethod(current_circle.set_color,new_stable_circle_color,run_time=0.3))
                round_flip_animations.append(flip_sequence)
                pending_updates.append((node_idx,new_arrow,new_spin_direction))
            if round_flip_animations:
                self.play(*round_flip_animations)
                for idx,updated_arrow,updated_spin_dir in pending_updates:
                    arrow_mobjects[idx]=updated_arrow; node_spin_directions_vectors[idx]=updated_spin_dir
            if i_round < num_flip_rounds-1: self.wait(0.8)
            else: self.wait(0.4)
        self.play(FadeOut(spin_flip_subtitle)); self.wait(0.5)
        
        total_states_value = 2**N
        states_text_mobj = MathTex(rf"\text{{For }} N={N}\text{{, Total Possible States: }} 2^{{{N}}} = {total_states_value}", font_size=36)
        states_text_mobj.to_edge(DOWN, buff=0.7)
        self.play(Write(states_text_mobj)); self.wait(3)

# Scene 2: Enumerating All Possible Spin States for N=5
# (Unchanged)
class IsingStatesEnumerationN5(Scene):
    def construct(self):
        N = 5; num_total_states = 2**N; UP_ARROW_COLOR = BLUE_C; DOWN_ARROW_COLOR = RED_C 
        title_text = rf"\text{{All }} 2^{{{N}}} = {num_total_states} \text{{ Possible Spin States for N=}}{{{N}}}"
        title = MathTex(title_text, font_size=40).to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.5)
        num_cols=8; num_rows=(num_total_states+num_cols-1)//num_cols
        state_arrow_length=0.25; state_arrow_half_length=state_arrow_length/2.0
        state_arrow_stroke_width=3.5; state_arrow_tip_ratio=0.4; all_state_groups=VGroup()
        for spin_config_tuple in itertools.product([0,1],repeat=N):
            single_state_representation=VGroup()
            for spin_value in spin_config_tuple:
                direction = UP if spin_value==1 else DOWN
                color = UP_ARROW_COLOR if spin_value==1 else DOWN_ARROW_COLOR
                arrow=Arrow(start=-direction*state_arrow_half_length,end=direction*state_arrow_half_length,buff=0,stroke_width=state_arrow_stroke_width,max_tip_length_to_length_ratio=state_arrow_tip_ratio,color=color)
                single_state_representation.add(arrow)
            single_state_representation.arrange(RIGHT,buff=state_arrow_length*0.25); all_state_groups.add(single_state_representation)
        all_state_groups.arrange_in_grid(rows=num_rows,cols=num_cols,buff=MED_SMALL_BUFF*0.8)
        if all_state_groups.height>(self.camera.frame_height-title.height-1.0): all_state_groups.scale_to_fit_height(self.camera.frame_height-title.height-1.2)
        if all_state_groups.width>(self.camera.frame_width-0.8): all_state_groups.scale_to_fit_width(self.camera.frame_width-1.0)
        all_state_groups.next_to(title,DOWN,buff=0.5)
        state_creation_animations=[GrowFromCenter(state_group) for state_group in all_state_groups]
        self.play(LaggedStart(*state_creation_animations,lag_ratio=0.015,run_time=max(3.5,0.07*num_total_states))); self.wait(4)