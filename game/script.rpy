image bg room = "room.png"

# Funder/institution logos shown on the disclaimer screen.
# Put the three logo files in game/images/ named exactly: logo_uum.png, logo_kpt.png, logo_ums.png
# (PNG with transparent background works best). ysize sets a common height; spacing is the gap between them.
image logos_row = HBox(
    Transform("logo_uum.png", fit="contain", ysize=160),
    Transform("logo_kpt.png", fit="contain", ysize=160),
    Transform("logo_ums.png", fit="contain", ysize=160),
    spacing=80,
)

#kucing tukar position
image room_cat_wake = Transform("room_catWakeup.png", xysize=(1920, 1080), fit="cover")
image room_cat_walk = Transform("room_catwalkaway.png", xysize=(1920, 1080), fit="cover")
image room_cat_shelf = Transform("room_catonshelf.png", xysize=(1920, 1080), fit="cover")
image bg room_cat:
    "room_cat_wake"
    pause 2.5
    "room_cat_walk"
    pause 1.6
    "room_cat_shelf"
image hana neutral = "Sprites/Neutral.png"
image hana smiling = "Sprites/Smiling.png"
image hana thinking:
    "Sprites/Thinking.png"
    pause renpy.random.uniform(0.6, 1.4)
    block:
        "Sprites/thinking_eyeclose.png"
        zoom 2.51
        pause 0.18
        "Sprites/Thinking.png"
        zoom 1.0
        pause renpy.random.uniform(2.4, 5.0)
        repeat
image hana sad = "Sprites/Sad.png"
image hana empathetic high = "Sprites/Empathetic high.png"
image hana empathetic low = "Sprites/Empathetic low.png"
image hana warm high = "Sprites/Warm high.png"
image hana warm low = "Sprites/Warm low.png"
image hana concerned high = "Sprites/Concerned high.png"
image hana concerned low = "Sprites/Concerned low.png"
image hana encouraging = "Sprites/Encouraging.png"
image hana good job = "Sprites/Good job.png"
image hana waving = "Sprites/Waving.png"
image hana hello = "Sprites/Waving.png"
image hana listening:
    "Sprites/Listening.png"
    pause renpy.random.uniform(0.6, 1.4)
    block:
        "Sprites/Listening_eyeclose.png"
        pause 0.18
        "Sprites/Listening.png"
        pause renpy.random.uniform(2.4, 5.0)
        repeat
image hana surprised = "Sprites/Thinking.png"

# method hana wink
image hana thinking eyeclose = "Sprites/thinking_eyeclose.png"
image hana listening eyeclose = "Sprites/Listening_eyeclose.png"

# scene extra untuk imagine
image beach = "beautifulbeach.jpg"
image beachscene = Movie(play="video/beachscene.webm")
image breathing_guide = Movie(play="video/478breathing.webm", loop=True)

# --- Hana Location transforms ---
transform hana_center:
    zoom 0.7
    xalign 1.0
    yanchor 0.925
    ypos 0.993

    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

transform hana_transition:
    zoom 0.7
    xalign 0.5
    yanchor 0.925
    ypos 0.993
    
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

transform hana_quick_change:
    zoom 0.7
    xalign 0.5
    yanchor 0.925
    ypos 0.993
    linear 0.15 alpha 0.5
    linear 0.15 alpha 1.0

transform hana_center_listen:
    zoom 1.82
    xalign renpy.random.choice([0.10, 0.22, 0.34])
    yanchor 0.912
    ypos 0.993

    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

# --- Random scene position transforms ---
transform hana_left:
    zoom 0.7
    xalign 0.1
    yanchor 0.925
    ypos 0.993
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

transform hana_mid:
    zoom 0.7
    xalign 0.5
    yanchor 0.925
    ypos 0.993
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

transform hana_right:
    zoom 0.7
    xalign 0.9
    yanchor 0.925
    ypos 0.993
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        linear 0.15 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.3 alpha 0.0

# guna bila method imaginary
transform scene_right:
    zoom 0.5
    xalign 0.95
    yalign 0.5
    on show:
        alpha 0.0
        xoffset 80
        linear 0.6 alpha 1.0 xoffset 0
    on replace:
        linear 0.2 alpha 1.0 xoffset 0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0 xoffset 80

transform breathing_guide_pos:
    zoom 0.5
    xalign 0.9
    yalign 0.42
    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0

init python:
    import math
    import random
    import datetime, csv, uuid, os

    def _hana_writable_log_dir():
        candidates = []
        for base in (getattr(config, "basedir", None), getattr(config, "savedir", None)):
            if base:
                candidates.append(os.path.join(base, "logs"))
        for d in candidates:
            try:
                os.makedirs(d, exist_ok=True)
                test = os.path.join(d, ".write_test")
                with open(test, "w") as _wf:
                    _wf.write("ok")
                os.remove(test)
                return d
            except Exception:
                continue
        try:
            import tempfile
            d = os.path.join(tempfile.gettempdir(), "hana_logs")
            os.makedirs(d, exist_ok=True)
            return d
        except Exception:
            return getattr(config, "savedir", ".") or "."

    DROPBOX_LOG_DIR = _hana_writable_log_dir()

    def generate_session_id():
        return str(uuid.uuid4())[:8]

    def make_session_filename():
        return f"session_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    def log_interaction(session_filename, session_id, question, answer,
                        score=None, stress_level=None,
                        Ea=None, Ec=None, Ad=None, Be=None, D=None, Ep=None,
                        empathy_mode=None):

        log_path = os.path.join(DROPBOX_LOG_DIR, session_filename)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = [
            timestamp, session_id, question, answer, score, stress_level,
            Ea, Ec, Ad, Be, D, Ep, empathy_mode
        ]

        try:
            write_header = not os.path.exists(log_path)
            with open(log_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow([
                        "timestamp","session_id","question","answer","score",
                        "stress_level","Ea","Ec","Ad","Be","D","Ep","empathy_mode"
                    ])
                writer.writerow(row)
        except Exception:
            pass  
        try:
            hana_sync_interaction(
                session_id, session_filename, timestamp, question, answer,
                score, stress_level, Ea, Ec, Ad, Be, D, Ep, empathy_mode,
            )
        except Exception:
            pass

    def log_interaction_enhanced(session_filename, session_id, question, answer,
                        score=None, stress_level=None,
                        Ea=None, Ec=None, Ad=None, Be=None, D=None, Ep=None,
                        empathy_mode=None, Ea_history=None, user_struggles=None, 
                        struggle_intensity=None, mode_shift_count=None, current_mode=None):
        
        log_path = os.path.join(DROPBOX_LOG_DIR, session_filename)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format Ea_history for logging
        ea_hist_str = "|".join([f"{x:.3f}" for x in (Ea_history or [])]) if Ea_history else ""
        
        row = [
            timestamp, session_id, question, answer, score, stress_level,
            Ea, Ec, Ad, Be, D, Ep, empathy_mode,
            ea_hist_str, user_struggles, struggle_intensity, mode_shift_count, current_mode
        ]
        
        try:
            write_header = not os.path.exists(log_path)
            with open(log_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow([
                        "timestamp","session_id","question","answer","score",
                        "stress_level","Ea","Ec","Ad","Be","D","Ep","empathy_mode",
                        "Ea_history","user_struggles","struggle_intensity","mode_shift_count","current_mode"
                    ])
                writer.writerow(row)
        except Exception:
            pass  

        try:
            hana_sync_interaction(
                session_id, session_filename, timestamp, question, answer,
                score, stress_level, Ea, Ec, Ad, Be, D, Ep, empathy_mode,
                extra={
                    "Ea_history": ea_hist_str,
                    "user_struggles": user_struggles,
                    "struggle_intensity": struggle_intensity,
                    "mode_shift_count": mode_shift_count,
                    "current_mode": current_mode,
                },
            )
        except Exception:
            pass

    def log_session_summary(session_filename, session_id, user_name,
                           start_stress_score, end_stress_score,
                           modes_used, techniques_used, total_interactions,
                           final_calm_rating, session_duration_minutes, end_action,
                           stress_improvement=None,
                           stress_level="", empathy_mode="", intention_level="",
                           empathy_E="", support_need_announced=""):


        log_path = os.path.join(DROPBOX_LOG_DIR, "session_summaries.csv")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # calculatee stress
        if stress_improvement is None:
            stress_improvement = start_stress_score - end_stress_score if start_stress_score else 0

        modes_str = "|".join(modes_used) if modes_used else "none"
        techniques_str = "|".join(techniques_used) if techniques_used else "none"

        row = [
            timestamp, session_id, user_name, start_stress_score, end_stress_score,
            stress_improvement, final_calm_rating, modes_str, techniques_str,
            total_interactions, session_duration_minutes, end_action,
            stress_level, empathy_mode, intention_level, empathy_E, support_need_announced
        ]

        header = [
            "timestamp", "session_id", "user_name", "start_stress_score", "end_stress_score",
            "stress_improvement", "final_calm_rating", "modes_used", "techniques_used",
            "total_interactions", "session_duration_minutes", "end_action",
            "stress_level", "empathy_mode", "intention_level", "empathy_E", "support_need_announced"
        ]
        pending_path = os.path.join(DROPBOX_LOG_DIR, "session_summaries_pending.csv")
        for target in (log_path, pending_path):
            try:
                write_header = not os.path.exists(target)
                with open(target, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    if write_header:
                        writer.writerow(header)
                    writer.writerow(row)
                break
            except Exception:
                continue
        try:
            hana_sync_summary(
                session_id, session_filename, timestamp, user_name,
                start_stress_score, end_stress_score, stress_improvement,
                final_calm_rating, modes_used, techniques_used,
                total_interactions, session_duration_minutes, end_action,
                stress_level, empathy_mode, intention_level,
                empathy_E, support_need_announced,
            )
        except Exception:
            pass


    def profile_key_for(name):
        return name.strip().lower()

    def default_user_profile(name):
        return {
            "name": name,
            "visit_count": 0,
            "last_session_id": "",
            "last_stress_score": None,
            "last_stress_level": "unknown",
            "last_empathy_mode": "unknown",
            "last_intention_level": "unknown",
            "last_empathy_E": 0.0,
            "last_calm_rating": None,
            "last_technique": None,
            "last_end_action": "",
            "support_need_announced": False,
            "music_enabled": None,  # None = never asked; True/False = saved preference
        }

    def load_user_profile(name):
        profile_store = getattr(persistent, "hana_user_memory", None) or {}
        key = profile_key_for(name)
        profile = default_user_profile(name)

        if key in profile_store:
            profile.update(profile_store[key])

        return key, profile_store, profile

    def save_user_profile(name, updates):
        profile_store = getattr(persistent, "hana_user_memory", None) or {}
        key = profile_key_for(name)
        profile = default_user_profile(name)

        if key in profile_store:
            profile.update(profile_store[key])

        profile.update(updates)
        profile_store[key] = profile
        persistent.hana_user_memory = profile_store
        return profile

#profile menu bole pilih
    PROFILE_SLOT_COUNT = 6

    def profile_slot_key(slot_index):
        return "slot_%d" % int(slot_index)

    def default_profile_slot(slot_index):
        return {
            "slot_index": int(slot_index),
            "profile_id": "",
            "name": "",
            "visit_count": 0,
            "last_session_id": "",
            "last_stress_level": "unknown",
            "last_calm_rating": None,
        }

    def load_profile_slot(slot_index):
        slot_store = getattr(persistent, "hana_profile_slots", None) or {}
        key = profile_slot_key(slot_index)
        slot = default_profile_slot(slot_index)

        if key in slot_store:
            slot.update(slot_store[key])

        return key, slot_store, slot

    def save_profile_slot(slot_index, updates):
        slot_store = getattr(persistent, "hana_profile_slots", None) or {}
        key = profile_slot_key(slot_index)
        slot = default_profile_slot(slot_index)

        if key in slot_store:
            slot.update(slot_store[key])

        slot.update(updates)
        slot_store[key] = slot
        persistent.hana_profile_slots = slot_store
        return slot

    def get_or_create_profile_id(slot_index):
        # Stable per-profile uuid, created the first time this slot is used and
        # kept until the slot is reset. A reset+reuse of the same slot yields a
        # NEW id, so the backend treats it as a different profile (no overwrite).
        key, slot_store, slot = load_profile_slot(slot_index)
        pid = (slot.get("profile_id", "") or "").strip()
        if not pid:
            pid = uuid.uuid4().hex
            save_profile_slot(slot_index, {"profile_id": pid})
        return pid

    def delete_profile_slot(slot_index):
        slot_store = getattr(persistent, "hana_profile_slots", None) or {}
        key = profile_slot_key(slot_index)

        slot = slot_store.get(key)
        if slot:
            name = (slot.get("name", "") or "").strip()
            if name:
                profile_store = getattr(persistent, "hana_user_memory", None) or {}
                pkey = profile_key_for(name)
                if pkey in profile_store:
                    del profile_store[pkey]
                    persistent.hana_user_memory = profile_store
            del slot_store[key]
            persistent.hana_profile_slots = slot_store

        renpy.restart_interaction()

    def cleanup_unfinished_profile_slots():
        slot_store = getattr(persistent, "hana_profile_slots", None) or {}
        profile_store = getattr(persistent, "hana_user_memory", None) or {}
        changed = False

        for i in range(1, PROFILE_SLOT_COUNT + 1):
            key = profile_slot_key(i)
            slot = slot_store.get(key)
            if not slot:
                continue
            name = (slot.get("name", "") or "").strip()
            if name and slot.get("visit_count", 0) <= 0:
                pkey = profile_key_for(name)
                # only drop the user memory if it also never completed a session
                if pkey in profile_store and profile_store[pkey].get("visit_count", 0) <= 0:
                    del profile_store[pkey]
                del slot_store[key]
                changed = True

        if changed:
            persistent.hana_profile_slots = slot_store
            persistent.hana_user_memory = profile_store

    def profile_slot_title(slot_index):
        dummy1, dummy2, slot = load_profile_slot(slot_index)
        name = slot.get("name", "").strip()

        if name:
            return name

        return "Profile %d" % int(slot_index)

    def profile_slot_summary(slot_index):
        dummy1, dummy2, slot = load_profile_slot(slot_index)
        visit_count = slot.get("visit_count", 0)
        last_stress_level = slot.get("last_stress_level", "unknown")
        last_calm_rating = slot.get("last_calm_rating", None)

        if visit_count <= 0 and last_stress_level == "unknown" and last_calm_rating is None:
            return "New slot"

        calm_text = "unknown" if last_calm_rating is None else str(last_calm_rating)
        return "Visits: %d | Stress: %s | Calm: %s" % (visit_count, last_stress_level, calm_text)

    def profile_save_page(slot_index):
        return "profile_%d" % int(slot_index)


    # --- Parameters for Affective Empathy Unit ---
    alpha_Ea = 0.7
    gamma_Ea = 0.15
    delta_Ea = 0.1
    Ea0 = 0.2

    # --- Parameters for Cognitive Empathy Unit ---
    alpha_Ec = 0.5
    gamma_Ec = 0.1
    delta_Ec = 0.1
    Ec0 = 0.2
    tau = 3

    # --- Parameters for Belief Unit ---
    alpha_Be = 0.4
    gamma_Be = 0.1
    beta_Be = 0.2
    delta_Be = 0.1
    Be0 = 0.1

    # --- Parameters for Desire Mechanism ---
    theta_be = 0.5
    theta_be_high = 0.8

    # --- Thresholds for Empathy Mode Selection ---
    theta_ec = 0.85
    theta_ad = 0.25

    # --- Parameters for Compassionate Empathy Unit ---
    alpha_Ep = 0.5
    delta_Ep = 0.05

    # --- Parameters for Adaptive Empathy Unit ---
    alpha_Ad = 0.6
    gamma_Ad = 0.1
    delta_Ad = 0.05
    Ad0 = 0.2

    # --- Integration and Intention ---
    w_ea = 0.4
    w_ec = 0.3
    w_ep = 0.3
    theta_c = 0.3
    theta_p = 0.7

    # --- Update functions ---
    def clamp01(x):
        return max(0.0, min(1.0, x))

    def clamp_range(x, lo, hi):
        return max(lo, min(hi, x))

    def update_affective(Ea, S, stress_level):
        if stress_level in ["Moderate", "Severe", "Extremely severe"]:
            dEa = alpha_Ea*S - gamma_Ea*Ea + delta_Ea*(Ea0 - Ea)
        else:
            dEa = -gamma_Ea*Ea + delta_Ea*(Ea0 - Ea)
        return clamp01(Ea + dEa)

    def update_cognitive(Ec, Ea_history):
        if len(Ea_history) == 0:
            Ea_prime = 0.0
        else:
            recent = Ea_history[-tau:]
            Ea_prime = sum(recent)/len(recent)
        dEc = alpha_Ec*Ea_prime - gamma_Ec*Ec + delta_Ec*(Ec0 - Ec)
        return clamp01(Ec + dEc)

    def update_belief(Be, S, Ec):
        dBe = alpha_Be*S - gamma_Be*Be + beta_Be*Ec + delta_Be*(Be0 - Be)
        return clamp01(Be + dBe)

    def desire(Be):
        return 1.0 if Be >= theta_be else 0.0

    def update_compassionate(Ea, Ec, D):
        combined = alpha_Ep*Ea + (1-alpha_Ep)*Ec
        decay = math.exp(-delta_Ep)
        return clamp01(combined * D * decay)

    def update_adaptive(Ad, Ea_history):
        if len(Ea_history) >= 2:
            slope = Ea_history[-1] - Ea_history[-2]
        else:
            slope = 0.0
        slope_pos = max(slope, 0.0)
        dAd = alpha_Ad * slope_pos - gamma_Ad * Ad + delta_Ad * (Ad0 - Ad)
        return clamp01(Ad + dAd)

    def action_potential(Ea, Ec, D, t=1.0, alpha_ep=0.5, delta_ep=0.05):
        return (alpha_ep*Ea + (1-alpha_ep)*Ec) * D * math.exp(-delta_ep * t)

    def integrate(Ea, Ec, Ep):
        ep_term = Ep if Ep is not None else 0.0
        return clamp01(w_ea*Ea + w_ec*Ec + w_ep*ep_term)

    def intention_score(E):
        if E >= theta_p:
            return 1.0
        elif E >= theta_c:
            return 0.5
        else:
            return 0.0

    def compassionate_category(Be, theta_be=0.5, theta_be_high=0.8):
        if Be >= theta_be_high:
            return "high"
        if Be >= theta_be:
            return "low"
        return None

    def select_empathy_mode(Ea, Ec, Ad, Be, allow_compassionate=True, situation_type=None, duration=None, 
                           adaptive_score=0, cognitive_score=0, compassionate_score=0):

        if compassionate_score >= 10 and situation_type == "event" and Ea >= 0.5:
            if allow_compassionate:
                comp = compassionate_category(Be)
                if comp == "high":
                    return "compassionate_high"
                if comp == "low":
                    return "compassionate_low"
        
 
        if adaptive_score >= 10 and situation_type == "ongoing" and duration == "long":
            if Ad >= 0.2:
                return "adaptive"
        

        if cognitive_score >= 10 and situation_type == "unclear":
            if Ec >= 0.5:
                return "cognitive"
        
        # Default priority logic
        if allow_compassionate:
            comp = compassionate_category(Be)
            if comp == "high" and Ea >= 0.55:
                return "compassionate_high"
            if comp == "low" and Ea >= 0.30:
                return "compassionate_low"
        if Ec >= 0.6:
            return "cognitive"
        if Ad >= 0.25:
            return "adaptive"
        return "affective"

    def intention_from_E(E):
        intent = intention_score(E)
        if intent >= 0.7:
            return "high"
        if intent >= 0.3:
            return "moderate"
        return "low"

    #method call facial expression tak hardcoded every line 
    def get_expression_for_mode(empathy_mode, intention_level, stress_level):
        expression_map = {
            # based on compass
            ("compassionate_high", "high"): "hana empathetic high",
            ("compassionate_high", "moderate"): "hana warm high",
            ("compassionate_high", "low"): "hana encouraging",
            
            ("compassionate_low", "high"): "hana warm high",
            ("compassionate_low", "moderate"): "hana warm low",
            ("compassionate_low", "low"): "hana smiling",
            
            # cognitive
            ("cognitive", "high"): "hana thinking",
            ("cognitive", "moderate"): "hana thinking",
            ("cognitive", "low"): "hana neutral",
            
            # adaptive
            ("adaptive", "high"): "hana concerned high",
            ("adaptive", "moderate"): "hana concerned low",
            ("adaptive", "low"): "hana neutral",
            
            # yang ni base punya flow
            ("affective", "high"): "hana empathetic low",
            ("affective", "moderate"): "hana neutral",
            ("affective", "low"): "hana smiling",
        }
        
        key = (empathy_mode, intention_level)
        expression = expression_map.get(key, "hana neutral")
        
        # express hana if user need help sangat2 or stress tinggi
        if stress_level in ["Severe", "Extremely severe"] and intention_level in ["high", "moderate"]:
            if empathy_mode not in ["compassionate_high", "compassionate_low"]:
                expression = "hana concerned high"
        
        return expression

    def classify_user_condition(stress_score_value, stress_level_value):
        if stress_level_value == "Extremely severe" or stress_score_value >= 34:
            return "Extremely severe distress"
        if stress_level_value == "Severe" or stress_score_value >= 26:
            return "Severe distress"
        if stress_level_value == "Moderate" or stress_score_value >= 19:
            return "Moderate distress"
        if stress_level_value == "Mild" or stress_score_value >= 15:
            return "Mild distress"
        return "Normal"

    def repeated_prolonged_distress_detected(condition, calm_rating_value, support_announced):
        if not support_announced:
            return False
        if calm_rating_value is None:
            return condition in ["Severe distress", "Extremely severe distress"]
        return calm_rating_value <= 2 and condition in ["Moderate distress", "Severe distress", "Extremely severe distress"]

    def empathy_policy_weight(rule):
        policy = getattr(persistent, "hana_empathy_policy", None) or {}
        policy_key = "%s|%s|%s" % (rule.get("strategy", ""), rule.get("intensity", ""), rule.get("expression", ""))
        return policy.get(policy_key, {}).get("weight", 0.0)

    def table_rule_for_condition(condition, urgent=False, repeated=False):
        rule = base_table_rule_for_condition(condition, urgent=urgent, repeated=repeated)
        if not urgent and rule.get("tag") != "repeated_prolonged_distress":
            if empathy_policy_weight(rule) <= -0.3:
                gentler = base_table_rule_for_condition(condition, urgent=False, repeated=True)
                gentler["tag"] = rule.get("tag", "") + "_policy_adjusted"
                return gentler

        return rule

    def base_table_rule_for_condition(condition, urgent=False, repeated=False):
        if urgent:
            return {
                "strategy": "Emergency empathic intervention",
                "intensity": "Immediate High",
                "intensity_bucket": "high",
                "mode": "compassionate_high",
                "expression": "hana concerned high",
                "tag": "reactive_support",
                "dialogue": [
                    "Hey, I'm right here. We're going to go slowly, okay?",
                    "I've got you. Let's just take this one small step.",
                    "You don't have to figure this out alone right now."
                ],
            }

        if repeated:
            return {
                "strategy": "Adaptive moderated support",
                "intensity": "Moderate",
                "intensity_bucket": "moderate",
                "mode": "adaptive",
                "expression": "hana encouraging",
                "tag": "repeated_prolonged_distress",
                "dialogue": [
                    "Let's keep this gentle — no pressure, just steady.",
                    "We can go slow. There's no rush here.",
                    "I'm still here with you, and we'll take this at whatever pace works."
                ],
            }

        if condition == "Normal":
            return {
                "strategy": "Passive empathic presence",
                "intensity": "Low",
                "intensity_bucket": "low",
                "mode": "affective",
                "expression": "hana neutral",
                "tag": "normal_presence",
                "dialogue": [
                    "I'm here. We can just take it easy.",
                    "No rush, no pressure — just whatever feels right.",
                    "I'm here and I'm listening to you."
                ],
            }

        if condition == "Mild distress":
            return {
                "strategy": "Emotional reassurance",
                "intensity": "Low–Moderate",
                "intensity_bucket": "moderate",
                "mode": "compassionate_low",
                "expression": "hana warm low",
                "tag": "mild_reassurance",
                "dialogue": [
                    "Yeah, that makes sense. It's okay to feel that way.",
                    "I hear you. We don't have to rush through it.",
                    "That's real, and you don't need to push past it right now."
                ],
            }

        if condition == "Moderate distress":
            return {
                "strategy": "Supportive guidance",
                "intensity": "Moderate",
                "intensity_bucket": "moderate",
                "mode": "adaptive",
                "expression": "hana thinking",
                "tag": "moderate_guidance",
                "dialogue": [
                    "Okay, let's slow down and look at this together.",
                    "I'm paying attention. We'll work through it piece by piece.",
                    "You're not doing this alone, we'll figure it out step by step."
                ],
            }

        if condition == "Severe distress":
            return {
                "strategy": "Active empathic support",
                "intensity": "Moderate–High",
                "intensity_bucket": "high",
                "mode": "adaptive",
                "expression": "hana concerned low",
                "tag": "severe_support",
                "dialogue": [
                    "That sounds really hard, and I don't want to rush past it.",
                    "I'm with you in this, let's be careful about how we move forward.",
                    "You deserve real support right now, not just words."
                ],
            }

        return {
            "strategy": "Intensive empathic intervention",
            "intensity": "High",
            "intensity_bucket": "high",
            "mode": "compassionate_high",
            "expression": "hana concerned high",
            "tag": "extreme_support",
            "dialogue": [
                "That sounds incredibly heavy. I'm not going anywhere.",
                "I'm here, and we're going to take this very gently.",
                "You don't have to carry this moment by yourself."
            ],
        }

    def feedback_signal_from_rating(calm_rating_value):
        if calm_rating_value is None:
            return "neutral"
        if calm_rating_value <= 2:
            return "negative"
        if calm_rating_value >= 4:
            return "positive"
        return "neutral"

    def update_empathy_policy_from_feedback(strategy_name, intensity_name, expression_name, feedback_signal):
        policy = getattr(persistent, "hana_empathy_policy", None) or {}

        policy_key = "%s|%s|%s" % (strategy_name, intensity_name, expression_name)
        current = policy.get(policy_key, {"weight": 0.0, "positive": 0, "negative": 0, "neutral": 0})

        if feedback_signal == "positive":
            current["positive"] += 1
            current["weight"] = clamp_range(current["weight"] + 0.1, -1.0, 1.0)
        elif feedback_signal == "negative":
            current["negative"] += 1
            current["weight"] = clamp_range(current["weight"] - 0.1, -1.0, 1.0)
        else:
            current["neutral"] += 1
            current["weight"] = clamp_range(current["weight"] + 0.01, -1.0, 1.0)

        policy[policy_key] = current
        persistent.hana_empathy_policy = policy
        return current

    def get_animation_transition():
        return "hana_transition"

    def get_quick_expression_change():
        return "hana_quick_change"

    def adapt_weights_from_feedback(calm_rating, s_in):
        global alpha_Ea, alpha_Ec, alpha_Ad, alpha_Be, alpha_Ep
        global w_ea, w_ec, w_ep, theta_be, theta_be_high

        if calm_rating <= 2:
            # User still stress
            alpha_Ea = clamp_range(alpha_Ea + 0.02, 0.20, 1.20)
            alpha_Ec = clamp_range(alpha_Ec + 0.015, 0.20, 1.20)
            alpha_Ad = clamp_range(alpha_Ad + 0.015, 0.20, 1.20)
            alpha_Be = clamp_range(alpha_Be + 0.01, 0.10, 1.00)
            alpha_Ep = clamp_range(alpha_Ep + 0.01, 0.05, 0.60)

            theta_be = clamp_range(theta_be - 0.01, 0.25, 0.80)
            theta_be_high = clamp_range(theta_be_high - 0.01, 0.50, 0.95)

        elif calm_rating >= 4:
            # User calmer
            alpha_Ea = clamp_range(alpha_Ea - 0.01, 0.20, 1.20)
            alpha_Ec = clamp_range(alpha_Ec - 0.008, 0.20, 1.20)
            alpha_Ad = clamp_range(alpha_Ad - 0.008, 0.20, 1.20)
            alpha_Be = clamp_range(alpha_Be - 0.005, 0.10, 1.00)
            alpha_Ep = clamp_range(alpha_Ep - 0.005, 0.05, 0.60)

            theta_be = clamp_range(theta_be + 0.005, 0.25, 0.80)
            theta_be_high = clamp_range(theta_be_high + 0.005, 0.50, 0.95)

    EMPATHY_PARAM_DEFAULTS = {
        "alpha_Ea": 0.7,
        "gamma_Ea": 0.15,
        "delta_Ea": 0.1,
        "Ea0": 0.2,
        "alpha_Ec": 0.5,
        "gamma_Ec": 0.1,
        "delta_Ec": 0.1,
        "Ec0": 0.2,
        "alpha_Be": 0.4,
        "gamma_Be": 0.1,
        "beta_Be": 0.2,
        "delta_Be": 0.1,
        "Be0": 0.1,
        "theta_be": 0.5,
        "theta_be_high": 0.8,
        "alpha_Ep": 0.5,
        "delta_Ep": 0.05,
        "alpha_Ad": 0.6,
        "gamma_Ad": 0.1,
        "delta_Ad": 0.05,
        "Ad0": 0.2,
        "w_ea": 0.4,
        "w_ec": 0.3,
        "w_ep": 0.3,
    }

    def show_hana_with_fade(expression, at_position="hana_center"):
        renpy.show(f"hana {expression} at {at_position}")
        renpy.transition(hana_quick_change)

    def reset_empathy_parameters():
        g = globals()
        for key, value in EMPATHY_PARAM_DEFAULTS.items():
            g[key] = value

    def select_empathy_mode_for_session(Ea, Ec, Ad, Be, allow_compassionate=True):
        st = renpy.store
        return select_empathy_mode(
            Ea, Ec, Ad, Be,
            allow_compassionate=allow_compassionate,
            situation_type=st.situation_type,
            duration=st.duration,
            adaptive_score=st.adaptive_score,
            cognitive_score=st.cognitive_score,
            compassionate_score=st.compassionate_score,
        )

    def pick_random_scene_pos():
        return renpy.random.choice([hana_left, hana_mid, hana_right])

    def infer_screening_context(checkin_signals):
        if not checkin_signals:
            return

        st = renpy.store
        peak = max(checkin_signals)
        avg = sum(checkin_signals) / float(len(checkin_signals))

        st.adaptive_score = 0
        st.cognitive_score = 0
        st.compassionate_score = 0
        st.situation_type = None
        st.duration = None

        if peak >= 1.0:
            st.situation_type = "event"
            st.compassionate_score = 12
        elif avg >= 0.5:
            st.situation_type = "ongoing"
            st.duration = "long"
            st.adaptive_score = 12
        elif avg >= 0.33:
            st.situation_type = "unclear"
            st.cognitive_score = 12
        else:
            st.situation_type = "event"
            st.duration = "short"
            st.adaptive_score = 4
            st.cognitive_score = 4
            st.compassionate_score = 4
# method nak clean menu function sebab nak bg main menu clear and bukan ingame
init 999 python:
    cleanup_unfinished_profile_slots()

default support_need_announced = False
default compassion_cooldown_steps = 0
default last_calm_rating = None
default calm_rated_this_session = False
default last_technique = None
default calming_done = False  
default feedback_given = False  
default avoid_technique_first = None  
default struggle_intensity = 0  
default mode_shift_reason = "" 
default quick_menu = True

# --- Characters ---
define e = Character("Hana", color="#b56ab3")

# =========================
# STATE VARIABLES
# =========================
default Ea = 0.2
default Ec = 0.2
default Be = 0.1
default Ep = 0.0
default E = 0.0
default I = 0.0
default D = 0.0
default S = 0.0
default stress_level = "Normal"
default stress_level_desc = "Normal"
default Ea_history = []
default Ad = 0.2
default last_empathy_mode = "unknown"
default day_impact = ""
default routine_stress = ""
default extra_weight = ""

default turn_id = 0
default feedback = 0.0
default system_response = ""
default user_input = ""

default modes_used_list = []  # Track all modes used in session
default techniques_used_list = []  # Track all techniques used in session
default session_start_stress = 0  # Initial stress score
default initial_stress_score = 0  # For reference
default interaction_count = 0  # Count of logged interactions
default session_start_time = None  # Track session duration

default session_id = ""
default session_filename = ""

default emotional_state = "unsure"
default last_intention_level = "unknown"
default last_empathy_E = 0.0

# --- Screening & Tracking Variables ---
default situation_type = None
default duration = None
default initial_empathy_hint = None

# --- Adaptive, Cognitive, Compassionate Screening (Binary + Hierarchical) ---
default adaptive_score = 0
default cognitive_score = 0
default compassionate_score = 0
default compassionate_level = "Low"  # Low or High (determined during screening)

# --- Mode Progression Tracking ---
default initial_empathy_profile = "Adaptive"  # Where user starts based on screening
default current_empathy_mode = "Adaptive"  # What mode HANA is currently using (can change)
default empathy_progression = ["Adaptive", "Cognitive", "Compassionate"]  # The progression path
default current_progression_index = 0  # Position in progression (0=Adaptive, 1=Cognitive, 2=Compassionate)
default mode_shift_count = 0  # Track how many times mode has shifted
default user_struggles = False  

default initial_stress_level = "Normal"
default initial_empathy_mode = "unknown"
default initial_Ea = 0.2
default stress_score = 0
default checkin_s_in_history = []
default hana_selected_profile_slot = 1
default hana_active_profile_id = ""
default hana_pos = hana_mid

# --- Flow Starts ---


# fade transition ubah muka
label hana_wave:
    show hana waving at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_smile:
    show hana smiling at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_listen:
    show hana listening at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_listen_wink:
    show hana listening at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_thinking_wink:
    show hana thinking at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_neutral:
    show hana neutral at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_concern_low:
    show hana concerned low at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_concern_high:
    show hana concerned high at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_encouraging:
    show hana encouraging at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label hana_good_job:
    show hana good job at hana_pos
    with Fade(0.3, 0.0, 0.3)
    return

label start:

    scene black
    with fade

    show logos_row:
        xalign 0.5 yalign 0.9
    centered "Disclaimer:\n\nThis session includes some questions about stress from the Depression Anxiety Stress Scales (DASS). \
    These questions are used for research only. They are not a medical test and cannot diagnose or treat mental health conditions.\n\n{size=-10}This research was supported by the Ministry of Higher Education (MoHE) of Malaysia through the Fundamental Research Grant Scheme (FRGS/1/2024/ICT02/UUM/02/1){/size}"
    hide logos_row

    scene bg room_cat
    show black:
        alpha 0.6
    with fade
#ni critical part if error sume tak jalan
    # nak clear slot yang session tak settle abis
    $ cleanup_unfinished_profile_slots()
    $ session_id = generate_session_id()
    $ session_filename = make_session_filename()
    $ reset_empathy_parameters()
    $ checkin_s_in_history = []
    $ adaptive_score = 0
    $ cognitive_score = 0
    $ compassionate_score = 0
    $ situation_type = None
    $ duration = None
    $ modes_used_list = []
    $ techniques_used_list = []
    $ interaction_count = 0
    $ calming_done = False
    $ calm_rated_this_session = False
    $ feedback_given = False
    $ session_start_time = datetime.datetime.now()
    $ selected_slot = clamp_range(hana_selected_profile_slot, 1, PROFILE_SLOT_COUNT)
    $ dummy1, dummy2, selected_slot_data = load_profile_slot(selected_slot)
    $ user_name = selected_slot_data.get("name", "").strip()
    $ hana_selected_profile_slot = selected_slot
    $ hana_active_profile_id = get_or_create_profile_id(selected_slot)
    $ hana_pos = hana_mid

    if user_name:
        $ user_profile_key, user_profile_store, user_profile = load_user_profile(user_name)
    else:
        $ user_profile_key, user_profile_store, user_profile = None, None, {}
    $ is_returning_user = user_profile.get("visit_count", 0) > 0
    $ last_stress_level = user_profile.get("last_stress_level", "unknown")
    $ prev_calm_rating = user_profile.get("last_calm_rating", None)
    # carry last visit's state forward so repeated_prolonged_distress_detected() can fire
    $ last_calm_rating = prev_calm_rating
    $ support_need_announced = user_profile.get("support_need_announced", False)
    $ prev_technique = user_profile.get("last_technique", None)
    $ prev_empathy_mode = user_profile.get("last_empathy_mode", "unknown")
    $ prev_intention_level = user_profile.get("last_intention_level", "unknown")

    # guna dkt technique nnti nak avoid same user dpt technique sama
    $ avoid_technique_first = prev_technique

    # idea dr azizi mintak user preference if nk guna music ke tak
    $ music_pref = user_profile.get("music_enabled", None)
    if music_pref:
        play music "audio/BGM/Hana_lofi.mp3" volume 0.3 fadein 3.0 loop

    # 2 flow (user baru or lama)
    if is_returning_user:
    
        show hana waving at hana_pos
        e "Welcome back, [user_name]."
        show hana warm high at hana_pos
        with Fade(0.3, 0.0, 0.3)
        e "It's nice to see you again."
        if last_stress_level in ["Moderate", "Severe", "Extremely severe"]:
            show hana concerned low at hana_pos
            e "Last time, it seemed like you were having a difficult time."
        else:
            show hana smiling at hana_pos
            e "Last time, things seemed to be okay."
    else:
        
        show hana waving at hana_pos
        e "Hi, I'm Hana."
        if not user_name:
            show hana listening at hana_center_listen
            with Fade(0.3, 0.0, 0.3)
            e "What is your name?"
            show hana smiling at hana_pos
            $ user_name = renpy.input("")
            $ user_name = user_name.strip().title() if user_name.strip() else "friend"
            $ save_profile_slot(selected_slot, {"name": user_name})
            $ user_profile_key, user_profile_store, user_profile = load_user_profile(user_name)

        show hana listening at hana_center_listen
        with Fade(0.3, 0.0, 0.3)
        e "It's nice to meet you, [user_name]."
        show hana smiling at hana_pos
        with Fade(0.3, 0.0, 0.3)

        e "My name means \"flower\" in Japanese and \"happiness\" in Arabic."

        e "I hope we have a nice conversation."

        e "I am glad you are here."
       
        menu:
            "Nice to meet you too, Hana.":
                show hana warm high at hana_pos
                e "Thank you. I am happy to meet you too."

            "That is a nice name.":
                show hana smiling at hana_pos
                e "Thank you. I like my name too."

            "Hi":
                show hana warm high at hana_pos
                e "Hi. I am happy we can talk today."

    # line mintak user nak music ke tak
    if music_pref is None:
        show hana smiling at hana_pos
        with Fade(0.3, 0.0, 0.3)
        e "Before we continue, would you like some soft background music?"
        e "Some people find it relaxing, while others prefer silence. Both are okay."

        menu:
            "Yes, I would like music.":
                $ music_pref = True
                show hana smiling at hana_pos
                e "Okay. I will play soft music."
                play music "audio/BGM/Hana_lofi.mp3" volume 0.2 fadein 3.0 loop

            "No, I would like silence.":
                $ music_pref = False
                show hana neutral at hana_pos
                e "Okay. We will continue without music."

        $ user_profile = save_user_profile(user_name, {"music_enabled": music_pref})
        $ log_interaction(session_filename, session_id,
                          "Music preference", "music_on" if music_pref else "music_off",
                          None, None, Ea, Ec, Ad, Be, None, None, "preference")

    hide black
    with Dissolve(0.5)

 #greeting and check-in

    show hana listening at hana_center_listen

    e "So, [user_name], how do you feel today?"
    menu:
        "I feel good":
            $ ans = "I feel good"
            $ s_in = 0.0
            show hana smiling at hana_pos
            e "That is wonderful. I am happy to hear that."

        "I feel quite okay":
            $ ans = "I feel quite okay"
            $ s_in = 0.33
            show hana neutral at hana_pos
            e "That is nice to hear. I hope the rest of your day goes well."

        "I feel a little stressed":
            $ ans = "A bit stressed"
            $ s_in = 0.67
            show hana concerned low at hana_pos
            e "It sounds like you have a few things to deal with."

        "I feel very stressed":
            $ ans = "Really stressed"
            $ s_in = 1.0
            show hana concerned high at hana_pos
            e "That sounds like a lot to deal with. Thank you for sharing that with me."

    $ checkin_s_in_history.append(s_in)
    call empathy_step("How do you feel today?", ans, s_in, "checkin_q1", speak=False) from _checkin_q1

    show hana listening at hana_center_listen
    # function nak refer ans q1 tadi ikut flow
    $ bridge_line = hana_bridge(level_from_s_in(checkin_s_in_history[-1]))
    e "[bridge_line!t]"
    e "How has your day been so far?"
    menu:
        "I have been doing many things today":
            $ ans = "Being productive and getting things done"
            $ s_in = 0.0
            show hana good job at hana_pos
            $ response_line = renpy.random.choice([
                "It sounds like you have done many things today. Well done.",
                "That can feel good. It sounds like you had a productive day.",
                "It is nice to hear that you could focus and do what you needed to do."
            ])
            e "[response_line!t]"

        "I have been resting and having time for myself":
            $ ans = "Relaxing and enjoying some me-time"
            $ s_in = 0.0
            show hana smiling at hana_pos
            $ response_line = renpy.random.choice([
                "That sounds nice. It is good to have some time for yourself.",
                "I am glad you had some time to rest. Those quiet moments are important.",
                "That sounds relaxing. It is good to give yourself some time to rest."
            ])
            e "[response_line!t]"

        "I feel tired from everything":
            $ ans = "Feeling exhausted from everything"
            $ s_in = 0.67
            show hana concerned low at hana_pos
            $ response_line = renpy.random.choice([
                "I am sorry to hear that. It sounds like today has made you very tired.",
                "That sounds tiring. It seems like many things needed your attention today.",
                "It sounds like you have low energy today. That can be hard."
            ])
            e "[response_line!t]"

        "Honestly, it has been a hard day":
            $ ans = "Honestly, it's been a rough day"
            $ s_in = 1.0
            show hana concerned high at hana_pos
            $ response_line = renpy.random.choice([
                "That sounds difficult. Some days can feel harder than others.",
                "I am sorry it has been that kind of day. Thank you for telling me.",
                "That sounds really hard. It is okay to say that today has been hard."
            ])
            e "[response_line!t]"

    $ checkin_s_in_history.append(s_in)
    call empathy_step("How has your day been so far?", ans, s_in, "checkin_q2", speak=False) from _checkin_q2

    show hana listening at hana_center_listen
    $ bridge_line = hana_bridge(level_from_s_in(checkin_s_in_history[-1]))
    e "[bridge_line!t]"
    e "Did anything make you feel stressed or upset today?"
    menu:
        "Not really":
            $ ans = "Not really"
            $ s_in = 0.0
            show hana smiling at hana_pos
            $ response_line = renpy.random.choice([
                "I am glad to hear that. It sounds like today was okay.",
                "That is good to know. It sounds like things were calm for you.",
                "I am glad today was not too stressful for you."
            ])
            e "[response_line!t]"

        "A little bit":
            $ ans = "A little bit"
            $ s_in = 0.33
            show hana neutral at hana_pos
            $ response_line = renpy.random.choice([
                "That makes sense. Small stresses can still affect your day.",
                "I understand. Even small problems can feel tiring.",
                "I see. Little things can still make the day harder."
            ])
            e "[response_line!t]"

        "Quite a lot":
            $ ans = "Quite a lot"
            $ s_in = 0.67
            show hana concerned low at hana_pos
            $ response_line = renpy.random.choice([
                "I am sorry to hear that. Feeling stressed for a long time can be tiring.",
                "That sounds tiring. It seems like today needed a lot from you.",
                "I understand. A stressful day can make you feel very tired."
            ])
            e "[response_line!t]"

        "Almost all day":
            $ ans = "Almost all day"
            $ s_in = 1.0
            show hana concerned high at hana_pos
            $ response_line = renpy.random.choice([
                "That sounds very tiring. It must have been hard to feel stressed for so long.",
                "I am sorry it lasted almost all day. That can be very hard.",
                "That sounds like a lot to deal with. Thank you for telling me."
            ])
            e "[response_line!t]"

    $ checkin_s_in_history.append(s_in)
    call empathy_step("Did anything make you feel stressed or upset today?", ans, s_in, "checkin_q3", speak=False) from _checkin_q3

    show hana encouraging at hana_pos
    $ bridge_line = hana_bridge(level_from_s_in(checkin_s_in_history[-1]))
    e "[bridge_line!t]"
    e "Now, I would like to ask about something positive."
    e "Even on a difficult day, there can still be something good."

    show hana listening at hana_center_listen
    e "What is one good thing that happened to you recently?"
    menu:
        "I did something important":
            $ ans = "I accomplished something important"
            $ s_in = 0.0
            show hana encouraging at hana_pos
            $ response_line = renpy.random.choice([
                "That is nice to hear. You should feel proud of what you did.",
                "Well done. Your hard work has paid off.",
                "I am glad to hear that. It is good to celebrate your achievements."
            ])
            e "[response_line!t]"

        "I had a nice time with someone":
            $ ans = "I had a nice moment with someone"
            $ s_in = 0.0
            show hana smiling at hana_pos
            $ response_line = renpy.random.choice([
                "That sounds nice. Spending time with people we care about is important.",
                "I am glad you had that time together.",
                "That is good to hear. A nice moment with someone can make a big difference."
            ])
            e "[response_line!t]"

        "I cannot think of anything":
            $ ans = "I can't really think of anything"
            $ s_in = 0.5
            show hana neutral at hana_pos
            $ response_line = renpy.random.choice([
                "That is okay. Some days it is hard to think of good things.",
                "That is alright. Sometimes the good moments are easy to miss.",
                "I understand. It is not always easy to think of something positive."
            ])
            e "[response_line!t]"

        "It has been hard lately":
            $ ans = "Honestly, it's been hard lately"
            $ s_in = 1.0
            show hana concerned high at hana_pos
            $ response_line = renpy.random.choice([
                "I am sorry to hear that. When things have been difficult for a while, it can be hard to see the good things.",
                "That sounds hard. When life has been difficult for a while, the good things can be hard to notice.",
                "I am sorry it has been that way. It takes strength to keep going through difficult times."
            ])
            e "[response_line!t]"

    $ checkin_s_in_history.append(s_in)
    call empathy_step("What is one good thing that happened to you recently?", ans, s_in, "checkin_q4", speak=False) from _checkin_q4
    $ infer_screening_context(checkin_s_in_history)

    show hana listening at hana_center_listen
    jump stress_input

label show_hana_empathy(empathy_mode, intention_level, stress_level, passive=False):
    if passive:
        $ _hana_expr = "hana listening"
    else:
        $ _hana_expr = get_expression_for_mode(empathy_mode, intention_level, stress_level)
    if _hana_expr == "hana listening":
        show expression _hana_expr at hana_center_listen
    else:
        show expression _hana_expr at hana_pos
    return

init python:
    # ni yang dr azizi request if HANA nk response..dia refer balik answer before so dia punya bridge line based on answer tu
    HANA_BRIDGES = {
        0: [
            "That's good to know. It sounds like things are going okay.",
            "It sounds like that is not causing you stress.",
            "I'm really glad to hear that.",
            "It sounds like that has not been too difficult for you.",
            "That is good to hear.",
            "It is good that this feels easier for you.",
            "I'm glad that has not been bothering you.",
            "It is nice to hear that things have been going okay.",
            "That is nice to hear.",
            "I'm glad that has not been too hard for you.",
            "It sounds like that has been easier for you."
        ],
        1: [
            "I see. Thank you for telling me.",
            "That makes sense. Thank you for sharing.",
            "Thank you for telling me that.",
            "It sounds like that happens sometimes.",
            "Thank you for sharing that with me.",
            "That is understandable. Many people feel that way.",
            "I understand what you mean.",
            "It sounds like that happens from time to time.",
            "That makes sense. I understand.",
            "I understand. I am here with you.",
            "It sounds like that is still on your mind."
        ],
        2: [
            "It sounds like you have been dealing with a lot.",
            "That cannot have been easy.",
            "I can see how that might affect you.",
            "It sounds like that has been on your mind.",
            "I can understand why that would be difficult for you.",
            "It sounds like that has been hard for you.",
            "It sounds like you have been dealing with that for some time.",
            "I can see how that would be tiring.",
            "It sounds like that has been difficult.",
            "That sounds like it has been hard to stop thinking about.",
            "I can imagine that has not been easy for you."
        ],
        3: [
            "It seems like you have been dealing with a lot lately.",
            "I can hear how much this has affected you.",
            "It sounds like this has not stopped.",
            "That sounds like a lot to deal with.",
            "That sounds very difficult.",
            "It sounds like it has been hard to get away from this.",
            "That seems like a lot to deal with on your own.",
            "I can see how much this has affected you.",
            "It sounds like this has been with you for some time.",
            "That sounds very tiring, day after day.",
            "I can only imagine how hard this has been for you."
        ],
    }
    _hana_bridge_remaining = {}

    def hana_bridge(prev_level):
        try:
            try:
                level = int(prev_level)
            except Exception:
                level = 1

            pool = HANA_BRIDGES.get(level, HANA_BRIDGES[1])
            if not pool:
                return "Okay."

            remaining = _hana_bridge_remaining.get(level)
            if not remaining:
                remaining = list(pool)

            line = renpy.random.choice(remaining)
            remaining.remove(line)
            _hana_bridge_remaining[level] = remaining
            return line
        except Exception:
            return "Okay."

    def level_from_s_in(s):
        try:
            s = float(s)
        except Exception:
            return 1
        if s >= 0.85:
            return 3
        elif s >= 0.6:
            return 2
        elif s >= 0.2:
            return 1
        return 0

# =======================================================
# Reusable empathy step:
#   1) Update Ea, Ec, Ad, Be from latest intensity signal s_in
#   2) Select empathy mode
#   3) Speak ONE inline empathy line of the matching type
#   4) Log everything
# =======================================================
label empathy_step(question, ans, s_in, phase, speak=True):

    $ Ea = update_affective(Ea, s_in, stress_level)
    $ Ea_history.append(Ea)
    $ Ea_history = Ea_history[-max(tau, 3):]
    $ Ec = update_cognitive(Ec, Ea_history)
    $ Ad = update_adaptive(Ad, Ea_history)
    $ Be = update_belief(Be, s_in, Ec)
    $ D = desire(Be)

    # Unified empathy state and intention thresholding.
    $ Ep_preview = update_compassionate(Ea, Ec, D) if D == 1.0 else 0.0
    $ E = integrate(Ea, Ec, Ep_preview)
    $ intention_level = intention_from_E(E)

    #check user condition based on stress lvl
    $ user_condition = classify_user_condition(stress_score, stress_level)

    #nak check urgent ke tak, high intention + extremely severe stress = urgent case
    $ urgent = (intention_level == "high" and stress_level == "Extremely severe")

    #check user problem dh lama ke tak
    $ repeated = repeated_prolonged_distress_detected(user_condition, last_calm_rating, support_need_announced)

    #based on table husna bagi mana empathetic strategy nak guna
    $ rule = table_rule_for_condition(user_condition, urgent=urgent, repeated=repeated)

    $ mode = rule.get("mode", "affective")
    $ last_empathy_mode = mode
    $ last_rule_tag = rule.get("tag", mode)
    $ last_intention_level = intention_level
    $ current_empathy_mode = mode

    # Track mode usage
    if mode not in modes_used_list:
        $ modes_used_list.append(mode)
    $ interaction_count += 1
    $ Ep = update_compassionate(Ea, Ec, D) if mode.startswith("compassionate") else None

    if speak:
        if intention_level == "low":
            call show_hana_empathy(mode, intention_level, stress_level, True) from _empathy_show_passive
        else:
            call show_hana_empathy(mode, intention_level, stress_level, False) from _empathy_show_active

        # generate dialogue line from rule dialogue pool
        $ line = renpy.random.choice(rule.get("dialogue", ["I'm here with you."]))
        e "[line!t]"

    # Update integrated empathy state and last found E
    $ E = integrate(Ea, Ec, Ep)
    $ last_empathy_E = E

    # Log with rule tag
    $ log_interaction(session_filename, session_id, question, ans,
                      None, None, Ea, Ec, Ad, Be, D, Ep, phase + "_" + rule.get("tag", mode))

    return


# --- Stress input capture ---
label stress_input:
    $ hana_pos = pick_random_scene_pos()

    $ fillers_before = [
        "Let's continue.",
        "Here is another question.",
        "I'd like to understand a little more.",
        "Let's look at this another way.",
        "Just a few more questions.",
        "Thank you for answering my questions."
    ]

    $ stress_questions = [
        "After a long day, is it hard for you to relax?",
        "Do small problems sometimes feel bigger than they really are?",
        "Do you ever feel nervous for no clear reason?",
        "Do you get restless more easily than usual?",
        "Is it hard for you to feel calm and relaxed?",
        "If something interrupts you, do you get frustrated quickly?",
        "Do you sometimes feel more sensitive than usual?",
    ]

    $ affective_feedback = {
        0: [
            "I'm really glad to hear that.",
            "That sounds okay, which is good.",
            "It's good to know that isn't causing too much trouble.",
            "That's good to hear.",
            "It sounds like you're handling that well.",
            "That's really good to hear from you.",
            "It sounds like that hasn't been bothering you too much.",
            "That's nice to hear.",
            "It sounds like things are going okay for you.",
            "It's good to know that hasn't been a big problem."
        ],
        1: [
            "That makes sense. Thank you for sharing.",
            "It's understandable to feel that way sometimes.",
            "I can see how that can happen sometimes.",
            "I understand that feeling.",
            "It sounds like it comes and goes.",
            "That's understandable. Many people feel that way.",
            "Many people go through that from time to time.",
            "That happens to many people.",
            "It sounds like it happens sometimes, but not all the time.",
            "It sounds like you're managing it, even though it isn't easy."
        ],
        2: [
            "That sounds difficult.",
            "I can see how that would be tiring.",
            "That can wear you out over time.",
            "It sounds like that's been on your mind."
            "That can't have been easy.",
            "I can understand why that feels tiring.",
            "That sounds like a lot to deal with.",
            "I can see how that could affect your day.",
            "That sounds hard to deal with.",
            "It seems like that's been taking a lot of your energy."
        ],
        3: [
            "That sounds really tiring.",
            "I'm sorry you've been going through that.",
            "That must be hard to deal with every day.",
            "It sounds like that's been affecting you a lot.",
            "That sounds really difficult.",
            "I can hear that this has been hard for you.",
            "That sounds like a lot for one person to deal with.",
            "I'm sorry things have been so difficult for you.",
            "It sounds like it's been hard to get away from that.",
            "That must be very tiring for you."
        ]
    }

    $ stress_responses = []
    $ i = 0

    while i < len(stress_questions):
        $ q = stress_questions[i]
        $ hana_pos = pick_random_scene_pos()
        show hana listening at hana_center_listen
        # Refer back to the previous answer before moving on, so it feels like
        # HANA is following along rather than reading off a checklist.
        if i == 0:
            e "[fillers_before[0]!t]"
        else:
            $ bridge_line = hana_bridge(stress_responses[i-1])
            e "[bridge_line!t]"
        e "[q!t]"

        menu:
            "Not really, that doesn't apply to me":
                $ stress_responses.append(0)
                $ ans = "Not really"
                $ s_in = 0.0
                show hana smiling at hana_pos
                $ response_line = renpy.random.choice(affective_feedback[0])
                e "[response_line!t]"

            "Maybe a little, once in a while":
                $ stress_responses.append(1)
                $ ans = "Maybe a little"
                $ s_in = 0.33
                show hana neutral at hana_pos
                $ response_line = renpy.random.choice(affective_feedback[1])
                e "[response_line!t]"

            "Yes, quite a lot of the time":
                $ stress_responses.append(2)
                $ ans = "Quite a lot"
                $ s_in = 0.67
                show hana concerned low at hana_pos
                $ response_line = renpy.random.choice(affective_feedback[2])
                e "[response_line!t]"

            "Almost always":
                $ stress_responses.append(3)
                $ ans = "Almost always"
                $ s_in = 1.0
                show hana concerned high at hana_pos
                $ response_line = renpy.random.choice(affective_feedback[3])
                e "[response_line!t]"

        call empathy_step(q, ans, s_in, "screening_q" + str(i+1), speak=False) from _screening_step

        show hana listening at hana_center_listen
        $ i += 1


    $ hi_count = sum(1 for r in stress_responses if r >= 2)
    if hi_count >= 4:
        show hana concerned high at hana_pos
        e "I am glad that we are here together."
        e "From your answers, it seems that things have been difficult for you lately."
    elif hi_count >= 1:
        show hana concerned low at hana_pos
        e "Thank you for answering these questions with me."
        e "I understand a little better how you have been feeling."
    else:
        show hana smiling at hana_pos
        e "Thank you for answering these questions."
        e "It sounds like things have been going well. I am glad to hear that."

    show hana listening at hana_center_listen

    # Compute scale from formula:
    # normalized_scale = raw_score / (number_of_items * max_item_score)
    # stress_score = normalized_scale * 42  (DASS-21 equivalent stress range)
    $ raw_score = sum(stress_responses)
    $ max_raw = float(len(stress_questions) * 3)
    $ stress_scale = (raw_score / max_raw) if max_raw > 0 else 0.0
    $ stress_score = int(round(stress_scale * 42.0))
    $ S = stress_scale
    $ session_start_stress = stress_score  
    $ initial_stress_score = stress_score  
    $ prev_end_stress = user_profile.get("last_stress_score", None) if user_profile else None
    if is_returning_user and prev_end_stress is not None:
        $ session_start_stress = prev_end_stress

    if stress_score <= 14:
        $ stress_level = "Normal"
        $ stress_level_desc = stress_level
        show hana smiling at hana_pos
    elif stress_score <= 18:
        $ stress_level = "Mild"
        $ stress_level_desc = stress_level
        show hana neutral at hana_pos
    elif stress_score <= 25:
        $ stress_level = "Moderate"
        $ stress_level_desc = stress_level
        show hana concerned low at hana_pos
    elif stress_score <= 33:
        $ stress_level = "Severe"
        $ stress_level_desc = stress_level
        show hana concerned low at hana_pos
    else:
        $ stress_level = "Extremely severe"
        $ stress_level_desc = stress_level
        show hana concerned high at hana_pos

    $ log_interaction(session_filename, session_id, "Stress score summary", str(raw_score),
                stress_score, stress_level_desc, Ea, Ec, Ad, Be, None, None, "stress_summary")

    # critical jugak nak decide reactive ke deliberative 
    # so nnti ada 2 flow which is reactive (straight to calming - Extremely severe) and deliberative (test affective/cognitive first - Moderate/Severe) and untuk Mild/Normal just straight to closure after screening
    $ D = desire(Be)
    $ Ep_now = update_compassionate(Ea, Ec, D) if D == 1.0 else 0.0
    $ E = integrate(Ea, Ec, Ep_now)
    $ intention_level = intention_from_E(E)
    $ last_intention_level = intention_level
    $ user_condition = classify_user_condition(stress_score, stress_level)
    $ urgent = (intention_level == "high" and stress_level == "Extremely severe")
    $ repeated = repeated_prolonged_distress_detected(user_condition, last_calm_rating, support_need_announced)
    $ rule = table_rule_for_condition(user_condition, urgent=urgent, repeated=repeated)
    $ last_empathy_mode = rule.get("mode", "affective")
    $ last_rule_tag = rule.get("tag", last_empathy_mode)
    $ current_empathy_mode = last_empathy_mode
    # penting dalam summary punya logs
    $ last_intention_level = rule.get("intensity_bucket", intention_level)
    if last_empathy_mode not in modes_used_list:
        $ modes_used_list.append(last_empathy_mode)
    if stress_level in ["Moderate", "Severe", "Extremely severe"]:
        $ support_need_announced = True

    # reactive path 
    if stress_level == "Extremely severe" or (stress_level == "Severe" and (intention_level == "high" or Ad >= 0.7)):
        show hana concerned high at hana_pos
        e "This sounds very difficult for you. If you feel very stressed, please call Befrienders at 03-7627 2929 or talk to someone you trust."
        show hana encouraging at hana_pos
        e "You do not have to face this alone. We do not need to talk about anything difficult now. Let us take a quiet moment together."
        call calming_loop from _reactive_calming_loop
        $ calming_done = True
        jump session_end_loop

    # deliberative path
    if stress_level in ["Moderate", "Severe"]:
        show hana concerned high at hana_pos
        e "If you are comfortable, could you tell me a little more about how this has affected you?"
        show hana listening at hana_center_listen
        call affective_input from _stress_affective_input
        jump session_end_loop

    # Normal or mild stress 
    else:
        jump session_end_loop


# option nk continue ke end

label session_end_loop:
    $ hana_pos = pick_random_scene_pos()
    $ session_done = False

    if calming_done:
        $ continue_session = True
        while continue_session:
            show hana warm high at hana_pos
            e "We have taken a quiet moment together. I am glad we did."
            show hana encouraging at hana_pos
            e "We can do another calming exercise, or we can stop here whenever you are ready."

            menu:
                "I want to continue a little longer":
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "continue_coping",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    call calming_loop from _continue_calming_loop

                "That is enough for me today":
                    if not feedback_given:
                        call post_response(last_empathy_mode) from _end_post_response
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "end_after_feedback",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    $ continue_session = False

        call phase5_close_update("exit_after_calming") from _phase5_after_calming
        return

    while not session_done:
        # Normal / Mild stress
        if stress_level in ["Normal", "Mild"]:
            show hana warm high at hana_pos

            if stress_level == "Normal":
                e "Before we finish, we can take a moment to do a simple breathing exercise together."
            else:
                e "Before we finish, we can try something simple to help you feel more relaxed."

            show hana encouraging at hana_pos
            e "Would you like to try a short breathing exercise with me?"

            menu:
                "Yes, let's try it":
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "continue_to_guidance",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    call calming_loop from _session_end_calming_loop
                    $ calming_done = True
                    if not feedback_given:
                        call post_response(last_empathy_mode) from _guided_post_response
                    call phase5_close_update("guided") from _phase5_after_guided
                    $ session_done = True

                "I'll stop here for today":
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "exit",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    call post_response(last_empathy_mode, "Was talking with me today helpful?") from _decline_post_response
                    call phase5_close_update("exit") from _phase5_exit
                    $ session_done = True

        # Moderate or severe yg tak lepas calming loop
        else:
            show hana concerned low at hana_pos
            e "It sounds like you have had a hard day."

            show hana encouraging at hana_pos
            e "Before we finish, we can try a short calming exercise together."

            show hana warm high at hana_pos
            e "It may help you feel calmer."

            menu:
                "Yes, let's try it":
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "continue_to_guidance",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    call calming_loop from _session_end_calming_loop_ms
                    $ calming_done = True
                    if not feedback_given:
                        call post_response(last_empathy_mode) from _guided_post_response_ms
                    call phase5_close_update("guided") from _phase5_after_guided_ms
                    $ session_done = True

                "I'll stop here for today":
                    $ log_interaction(
                        session_filename, session_id,
                        "Session menu", "exit",
                        stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None,
                        "session_loop"
                    )
                    call post_response(last_empathy_mode) from _decline_post_response_ms
                    call phase5_close_update("exit") from _phase5_exit_ms
                    $ session_done = True

    return

# --- Affective empathy input ---
label affective_input:
    $ hana_pos = pick_random_scene_pos()
    show hana listening at hana_center_listen
    $ D = None
    $ fillers_before_aff = [
        "I would like to understand a little more.",
        "Can you tell me a little more?",
        "Thank you for talking with me."
    ]
    $ affective_responses = []
    $ hana_pos = pick_random_scene_pos()
    show hana listening at hana_center_listen
    e "[fillers_before_aff[0]!t]"
    $ q = "How has this stress affected your everyday life recently?"
    e "[q!t]"

    menu:
        "It has been hard to focus on daily tasks.":
            $ day_impact = "focus"
            $ ans = "Hard to focus on daily tasks"
            $ aff_score = 1
            show hana neutral at hana_pos
            e "When you feel stressed, even simple tasks can feel harder."

        "I feel mentally drained most of the time.":
            $ day_impact = "drained"
            $ ans = "Mentally drained most of the time"
            $ aff_score = 3
            show hana concerned high at hana_pos
            e "Being mentally tired can make everything feel more difficult."

        "I keep worrying even when I try to do other things.":
            $ day_impact = "worry"
            $ ans = "Keeps worrying during other things"
            $ aff_score = 2
            show hana concerned low at hana_pos
            e "It can be hard when worry stays on your mind."

        "It has affected my sleep, rest, or mood.":
            $ day_impact = "sleep_mood"
            $ ans = "Affected sleep, rest, or mood"
            $ aff_score = 3
            show hana concerned high at hana_pos
            e "That sounds difficult. Sleep, rest, and mood can affect the whole day."

    $ affective_responses.append(aff_score)
    $ s_in = aff_score / 3.0
    call empathy_step(q, ans, s_in, "affective_followup_q1", speak=False) from _aff_followup_q1

    $ hana_pos = pick_random_scene_pos()
    show hana listening at hana_center_listen
    $ bridge_line = hana_bridge(affective_responses[0])
    e "[bridge_line!t]"
    $ q = "Which part of your daily routine has been the most stressful lately?"
    e "[q!t]"

    menu:
        "Balancing caregiving with work or study":
            $ routine_stress = "balance"
            $ ans = "Balancing caregiving with work or study"
            $ aff_score = 2
            show hana concerned low at hana_pos
            e "Balancing caregiving with work or study can be tiring when you have many responsibilities."

        "Managing household tasks and caregiving":
            $ routine_stress = "household"
            $ ans = "Managing household tasks and caregiving"
            $ aff_score = 2
            show hana concerned low at hana_pos
            e "Managing household tasks while caring for someone can make your day feel very busy."

        "Finding time for myself":
            $ routine_stress = "personal_time"
            $ ans = "Finding time for myself"
            $ aff_score = 1
            show hana neutral at hana_pos
            e "Not having enough time for yourself can slowly make you feel tired."

        "Handling unexpected situations while caring for someone":
            $ routine_stress = "unexpected_needs"
            $ ans = "Handling unexpected caregiving needs"
            $ aff_score = 3
            show hana concerned high at hana_pos
            e "Unexpected situations while caring for someone can make the day feel difficult to manage."

    $ affective_responses.append(aff_score)
    $ s_in = aff_score / 3.0
    call empathy_step(q, ans, s_in, "affective_followup_q2", speak=False) from _aff_followup_q2

    $ hana_pos = pick_random_scene_pos()
    show hana listening at hana_center_listen
    $ bridge_line = hana_bridge(affective_responses[1])
    e "[bridge_line!t]"
    $ q = "Has anything been making things more difficult for you lately?"
    e "[q!t]"

    menu:
        "Worrying about the person I care for":
            $ extra_weight = "care_recipient_worry"
            $ ans = "Worrying about the person I care for"
            $ aff_score = 2
            show hana concerned low at hana_pos
            e "Worrying about the person you care for can stay on your mind, even when you try to focus on other things."

        "Having too many responsibilities at once":
            $ extra_weight = "too_many_responsibilities"
            $ ans = "Having too many responsibilities at once"
            $ aff_score = 3
            show hana concerned high at hana_pos
            e "Having too many responsibilities at once can make it feel like you cannot rest."

        "Not getting enough rest or support":
            $ extra_weight = "lack_of_rest_support"
            $ ans = "Not getting enough rest or support"
            $ aff_score = 3
            show hana concerned high at hana_pos
            e "Not getting enough rest or support can make caregiving feel much harder."

        "Something else":
            $ extra_weight = "other"
            $ ans = "Something else"
            $ aff_score = 2
            show hana concerned low at hana_pos
            e "Even if it is hard to explain, your feelings still matter."

    $ affective_responses.append(aff_score)
    $ s_in = aff_score / 3.0
    call empathy_step(q, ans, s_in, "affective_followup_q3", speak=False) from _aff_followup_q3

    show hana listening at hana_center_listen

    if len(affective_responses) > 0:
        $ S_affective = sum(affective_responses) / (3.0 * len(affective_responses))
    else:
        $ S_affective = 0.0

    $ Ea = update_affective(Ea, S_affective, stress_level)
    $ Ea_history.append(Ea)
    $ Ea_history = Ea_history[-max(tau, 3):]
    $ Ec = update_cognitive(Ec, Ea_history)
    $ Ad = update_adaptive(Ad, Ea_history)

    $ log_interaction(session_filename, session_id, "Affective empathy update", str(S_affective),
                    stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "affective_update")

    $ high_aff = sum(1 for r in affective_responses if r >= 2)
    if high_aff >= 2:
        show hana concerned low at hana_pos
        e "Thank you for sharing that with me."
        e "It sounds like a few things have been making life harder for you lately."
    else:
        show hana warm high at hana_pos
        e "Thank you for sharing that with me."
        e "I understand a little better what has been causing your stress."

    if Ea < 0.35:
        e "It sounds like you've been managing it quite well."
    elif Ea < 0.65:
        e "It sounds like it's been affecting you more recently."
    else:
        e "It sounds like this has been affecting you for quite some time."

    # ADAPTIVE EMPATHY DISPLAY
    if Ad >= theta_ad:
        show hana concerned low at hana_pos
        e "I can see that some of these experiences have been affecting you."
        show hana encouraging at hana_pos
        e "There is no need to rush. We can take it one step at a time."
        $ log_interaction(session_filename, session_id,
                          "Empathy activation", "adaptive_start",
                          stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "adaptive")

    if Ea >= 0.6 or Ec >= theta_ec:
        show hana thinking at hana_pos
        e "I'd like to understand a little more about what has been making you feel this way."

        $ log_interaction(
            session_filename, session_id,
            "Empathy activation", "cognitive_start",
            stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "cognitive"
        )

        show hana listening at hana_center_listen
        e "When things start to feel difficult, which part is the hardest for you?"

        menu:
            "Balancing caregiving with other responsibilites":
                $ heavy_type = "balance"
            "Worrying about the person I care for":
                $ heavy_type = "worry"
            "Feeling emotionally or physically exhausted":
                $ heavy_type = "exhaustion"
            "Something else":
                $ heavy_type = "other"

        $ log_interaction(session_filename, session_id, "Heavy type selection", heavy_type,
                stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "cognitive")

        if heavy_type == "balance":
            show hana concerned low at hana_pos
            e "Balancing caregiving with other responsibilities can be very tiring. Let's focus on one small step at a time."

        elif heavy_type == "worry":
            show hana concerned low at hana_pos
            e "Caring for someone can bring a lot of worry. Let's take a moment to slow down and breathe together."

        elif heavy_type == "exhaustion":
            show hana concerned low at hana_pos
            e "It sounds like you've been giving a lot of your time and energy. It may be a sign that you've been carrying a lot."

        else:
            show hana concerned low at hana_pos
            e "Even if it's hard to explain, your feelings are still important. We can take things one step at a time."

        $ Be = update_belief(Be, S_affective, Ec)
        $ D = desire(Be)

        # 4 level intention kena decide
        if Be >= theta_be and D == 1.0:
            if Be >= theta_be_high:
                $ intention_type = "compassionate_high"
            else:
                $ intention_type = "compassionate_low"
        elif Ec >= 0.6:
            $ intention_type = "cognitive_reflection"
        elif Ad >= 0.25:
            $ intention_type = "adaptive_pacing"
        else:
            $ intention_type = None

        if compassion_cooldown_steps > 0 and intention_type in ["compassionate_high", "compassionate_low"]:
            if Ec >= 0.6:
                $ intention_type = "cognitive_reflection"
            elif Ad >= 0.25:
                $ intention_type = "adaptive_pacing"
            else:
                $ intention_type = None

        python:
            _delivered_mode = {
                "compassionate_high": "compassionate_high",
                "compassionate_low": "compassionate_low",
                "cognitive_reflection": "cognitive",
                "adaptive_pacing": "adaptive",
            }.get(intention_type, last_empathy_mode)
            last_empathy_mode = _delivered_mode
            current_empathy_mode = _delivered_mode
            last_intention_level = {
                "compassionate_high": "high",
                "compassionate_low": "moderate",
                "cognitive_reflection": "moderate",
                "adaptive_pacing": "low",
            }.get(intention_type, last_intention_level)
            if _delivered_mode not in modes_used_list:
                modes_used_list.append(_delivered_mode)

        if intention_type in ["compassionate_high", "compassionate_low"]:
            if intention_type == "compassionate_high":
                e "It sounds like you've been carrying a lot."
                e "Thank you for sharing this with me."
            else:
                e "Thank you for sharing that with me."
                e "Let's take it one step at a time."

            $ Ep = update_compassionate(Ea, Ec, D)

            $ log_interaction(
                session_filename, session_id,
                "Empathy activation", intention_type,
                stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, Ep, intention_type
            )
            call calming_loop from _comp_calming_loop
            $ calming_done = True

        elif intention_type == "cognitive_reflection":
            show hana thinking at hana_pos
            e "Thank you for helping me understand how you've been feeling."
            e "Before we continue, I'd like to think about what you've shared."
            $ log_interaction(
                session_filename, session_id,
                "Empathy activation", intention_type,
                stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "cognitive"
            )
            call calming_loop from _cog_calming_loop
            $ calming_done = True

        elif intention_type == "adaptive_pacing":
            show hana concerned low at hana_pos
            e "We can slow down whenever you need to."
            e "We'll go at a pace that feels comfortable for you."
            $ log_interaction(
                session_filename, session_id,
                "Empathy activation", intention_type,
                stress_score, stress_level_desc, Ea, Ec, Ad, Be, D, None, "adaptive"
            )
            call calming_loop from _adapt_calming_loop
            $ calming_done = True

        else:
            show hana concerned low at hana_pos
            e "It sounds like there may be more to what you've shared."
            show hana listening at hana_center_listen
            e "I'm right here with you, [user_name]."

    show hana listening at hana_center_listen
    return

# ===========================
# POST-RESPONSE FEEDBACK
# ===========================
label post_response(strategy="general", feedback_prompt="Did talking with me today help you?"):
    $ hana_pos = pick_random_scene_pos()
    show hana encouraging at hana_pos
    e "[feedback_prompt!t]"

    menu:
        "Yes":
            $ feedback = 1.0
            $ help_ans = "Yes"
        "A little":
            $ feedback = 0.5
            $ help_ans = "A little"
        "No":
            $ feedback = 0.0
            $ help_ans = "No"

    python:
        post_rating = {1.0: 5, 0.5: 3, 0.0: 1}[feedback]

        signal = feedback_signal_from_rating(post_rating)
        try:
            update_empathy_policy_from_feedback(rule.get("strategy", strategy), rule.get("intensity", "unknown"), rule.get("expression", "hana neutral"), signal)
        except Exception:
            update_empathy_policy_from_feedback(strategy, "unknown", "hana neutral", signal)

    $ log_interaction(
        session_filename, session_id,
        "Post-response feedback", help_ans,
        post_rating, stress_level, Ea, Ec, Ad, Be, D, None,
        "post_response_" + strategy
    )

    # closing line yg adapt dgn feedback conversation
    if signal == "negative":
        show hana concerned low at hana_pos
        $ fb_close = "I'm sorry things still feel difficult. Let's take things slowly from here."
        e "[fb_close!t] [user_name]."
    elif signal == "positive":
        show hana smiling at hana_pos
        $ fb_close = "I'm really glad that helped, even a little."
        e "[fb_close!t]"
    else:
        show hana warm high at hana_pos
        $ fb_close = "Thank you. We'll take things at a pace that feels right for you."
        e "[fb_close!t]"

    $ feedback_given = True  # user has now given feedback; session is allowed to end

    show hana listening at hana_center_listen
    return

#CALMING LOOP
label calming_loop:
    $ hana_pos = pick_random_scene_pos()
    $ loop_count = 0
    $ max_loops = 3
    $ techniques = ["breathing", "grounding", "body_scan", "gratitude", "reflection"]
    $ used_techniques = []
    $ calm_rating = 0
    $ should_exit = False

    while loop_count < max_loops:
        # Pick 2 techniques for this round
        $ available = [t for t in techniques if t not in used_techniques]
        if len(available) < 2:
            $ used_techniques = []
            $ available = list(techniques)

        # part guna technique beza beza untuk returning user
        $ first_choices = available
        if loop_count == 0 and avoid_technique_first in available and len(available) > 1:
            $ first_choices = [t for t in available if t != avoid_technique_first]

        $ tech1 = renpy.random.choice(first_choices)
        $ used_techniques.append(tech1)
        $ available = [t for t in available if t != tech1]
        $ tech2 = renpy.random.choice(available)
        $ used_techniques.append(tech2)
        $ last_technique = tech2

        # Deliver first technique
        call deliver_technique(tech1) from _deliver_tech_a

        # Brief bridge before second technique
        show hana encouraging at hana_pos
        e "Let's try one more. This one is a little different."

        # Deliver second technique
        call deliver_technique(tech2) from _deliver_tech_b

        # Ask calm state after both techniques
        show hana listening at hana_center_listen
        e "How are you feeling now, [user_name]?"
        menu:
            "I'm still very stressed":
                $ calm_rating = 1
                $ s_in = 1.0
                $ ans = "Still very stressed"
            "I'm still a bit stressed":
                $ calm_rating = 2
                $ s_in = 0.67
                $ ans = "A bit stressed"
            "I'm feeling a little better":
                $ calm_rating = 3
                $ s_in = 0.33
                $ ans = "Somewhere in between"
            "I'm feeling calmer":
                $ calm_rating = 4
                $ s_in = 0.1
                $ ans = "A little calmer"
            "I'm feeling much calmer":
                $ calm_rating = 5
                $ s_in = 0.0
                $ ans = "Much calmer"
            "I'd like to stop for now":
                $ should_exit = True
                $ ans = "I'd like to stop"

        if not should_exit:
            $ last_calm_rating = calm_rating
            $ calm_rated_this_session = True
            $ adapt_weights_from_feedback(calm_rating, s_in)
            $ signal = feedback_signal_from_rating(calm_rating)
            python:
                try:
                    update_empathy_policy_from_feedback(rule.get("strategy", last_empathy_mode), rule.get("intensity", "unknown"), rule.get("expression", "hana neutral"), signal)
                except Exception:
                    update_empathy_policy_from_feedback(last_empathy_mode, "unknown", "hana neutral", signal)

            $ Ea = max(0.0, Ea - 0.08)
            $ Ea = update_affective(Ea, s_in, stress_level)
            $ Ea_history.append(Ea)
            $ Ea_history = Ea_history[-max(tau, 3):]
            $ Ec = update_cognitive(Ec, Ea_history)
            $ Ad = update_adaptive(Ad, Ea_history)
            $ Be = update_belief(Be, s_in, Ec)
            $ D = desire(Be)
            $ E = integrate(Ea, Ec, 0.0)
            $ last_empathy_E = E
            python:
                _rank = {"low": 0, "moderate": 1, "high": 2}
                _now = intention_from_E(E)
                if _rank.get(_now, 0) > _rank.get(last_intention_level, 0):
                    last_intention_level = _now

            $ log_interaction(
                session_filename, session_id,
                "Calming loop rating after " + tech1 + "+" + tech2, ans,
                calm_rating, stress_level, Ea, Ec, Ad, Be, D, None,
                "calming_loop_iter" + str(loop_count + 1) + "_" + tech1 + "_" + tech2
            )

        $ loop_count += 1

        if should_exit:
            $ log_interaction(
                session_filename, session_id,
                "Calming loop ended (user stopped)", ans,
                None, stress_level, Ea, Ec, Ad, Be, D, None,
                "calming_loop_user_exit"
            )
            show hana encouraging at hana_pos
            $ exit_msg = renpy.random.choice([
                "That's okay. Thank you for giving this a try.",
                "No worries. Whenever you're ready, I'll be here.",
                "Take care of yourself. I'll be here whenever you want to talk again."
                ])
            e "[exit_msg!t]"
            return

        if calm_rating >= 4:
            show hana smiling at hana_pos
            $ calm_close = renpy.random.choice([
                "I'm glad you're feeling a little calmer.",
                "That's good to hear. You stayed with it, and that is important.",
                "It sounds like things have changed a little."
            ])
            e "[calm_close!t]"
            show hana encouraging at hana_pos
            e "Hold onto that, [user_name]. Be gentle with yourself today."
            if not feedback_given:
                call post_response(last_empathy_mode) from _calm_post_response_a
            return
        else:
            show hana encouraging at hana_pos
            $ keep_going = renpy.random.choice([
                "That's okay. These things can take time. Let's try something else.",
                "No rush. We can try a different exercise.",
                "That's alright. Let's take it one step at a time."
            ])
            e "[keep_going!t]"

    # if user reaches max calm loop but is still stressed
    show hana concerned low at hana_pos
    e "We tried a few things together, and thank you for staying with me."
    e "If things still feel difficult, please reach out to Befrienders (03-7627 2929) or talk to someone you trust."
    e "You do not have to go through this alone."
    show hana encouraging at hana_pos
    e "Thank you for spending this time with me today, [user_name]."
    $ log_interaction(
        session_filename, session_id,
        "Calming loop ended (max loops)", "rating=" + str(calm_rating),
        calm_rating, stress_level, Ea, Ec, Ad, Be, D, None,
        "calming_loop_max_reached"
    )
    if not feedback_given:
        call post_response(last_empathy_mode) from _calm_post_response_b
    return


# example techniques 
label deliver_technique(tech):
    $ hana_pos = pick_random_scene_pos()
    python:
        if tech not in techniques_used_list:
            techniques_used_list.append(tech)

    if tech == "breathing":
        show hana encouraging at hana_pos
        e "Let us start with a simple breathing exercise."
        e "When we feel stressed, we may breathe faster without noticing."
        e "Slow breathing can help the body feel calmer."
        # step Hana to the left for the breathing rounds
        $ hana_pos = hana_left
        show hana neutral at hana_pos
        e "Let's do it together at a comfortable pace."
        show breathing_guide at breathing_guide_pos
        python:
            renpy.show("hana encouraging", at_list=[hana_left])
            e(_("Breathe in slowly through your nose for four seconds."), interact=False)
            renpy.pause(4.0)
            e(_("Hold your breath for seven seconds."), interact=False)
            renpy.pause(7.0)
            e(_("Now breathe out slowly through your mouth for eight seconds."), interact=False)
            renpy.pause(8.0)
            # two full 4-7-8 breathing rounds
            for _round in range(2):
                renpy.show("hana encouraging", at_list=[hana_left])
                e(_("Breathe in. One, two, three, four."), interact=False)
                renpy.pause(4.0)
                renpy.show("hana neutral", at_list=[hana_left])
                e(_("Hold your breath. One, two, three, four, five, six, seven."), interact=False)
                renpy.pause(7.0)
                renpy.show("hana smiling", at_list=[hana_left])
                e(_("Breathe out. One, two, three, four, five, six, seven, eight."), interact=False)
                renpy.pause(8.0)
                if _round == 0:
                    renpy.show("hana good job", at_list=[hana_left])
                    e(_("There you go."), interact=False)
                    renpy.pause(2.0)
                    e(_("Let us do one more round."), interact=False)
                    renpy.pause(2.0)
        hide breathing_guide
        show hana smiling at hana_pos
        e "Well done. Even a few slow breaths can help you feel calmer."

    elif tech == "grounding":
        show hana encouraging at hana_pos
        e "This exercise is called the 5-4-3-2-1 grounding technique."
        e "When we feel stressed or overwhelmed, our minds can become very busy."
        e  "This exercise helps us focus on the present by noticing what we can see, hear, feel, smell, and taste."
        show hana neutral at hana_pos
        e "Take a moment to look around you. There's no need to rush."
        show hana encouraging at hana_pos
        e "First, notice 5 things you can see."
        e "Next, notice 4 things you can touch or feel, like your chair, your clothes, or your hands."
        e "Now, listen for 3 sounds around you. Even quiet sounds count."
        e "Then, notice 2 things you can smell, or remember smelling recently."
        e "Finally, notice 1 thing you can taste."
        show hana smiling at hana_pos
        e "Good job. Right now, you're here. Just focus on this moment."

    elif tech == "body_scan":
        show hana encouraging at hana_pos
        e "Let us try a short body scan exercise."
        e "Stress can sometimes affect the body without us noticing."
        e "You may feel tightness in your shoulders, jaw, neck, or hands."
        show hana neutral at hana_pos
        e "Take a moment to notice how your body feels."
        show hana encouraging at hana_pos
        e "Start with your shoulders. Let them relax."
        e "Now notice your jaw. Let it relax, and let your tongue rest."
        e "Next, notice your hands. Let them relax and rest."
        e "Now pay attention to the rest of your body."
        e "Notice your neck, chest, stomach, or any part that feels tight."
        show hana thinking at hana_pos
        e "If you notice a tight area, that's okay."
        e "You do not need to change anything right now."
        e "Just take a slow breath and notice how your body feels."
        show hana smiling at hana_pos
        e "Well done. Noticing tension can be the first step to letting it go."

    elif tech == "gratitude":
        show hana smiling at hana_pos
        e "Let us try a short gratitude exercise."
        show hana neutral at hana_pos
        e "When we feel stressed, we often focus on our problems and worries."
        e "Taking a moment to notice something positive can help us feel more balanced."
        show hana encouraging at hana_pos
        e "I'd like you to think of one thing that has made you feel good, comfortable, or happy recently."
        e "It does not have to be something big."
        e "It could be a nice conversation, a favourite meal, a quiet moment, or something that made you smile."
        show hana smiling at hana_pos
        e "Take a moment to think about it."
        e "Notice how it made you feel, and stay with that feeling for a few seconds."
        e "Sometimes small positive moments are worth remembering."

    elif tech == "reflection":
        stop music fadeout 2.0
        show beachscene at scene_right
        show hana neutral at hana_left
        e "Let us try a guided imagery exercise."
        e "This exercise helps you relax by focusing on a calm place."
        e "Many people find it helpful during stressful moments."
        show hana neutral at hana_left
        e "Take a moment to look at this peaceful beach."
        e "Imagine you are here, feeling safe and comfortable."
        show hana encouraging at hana_left
        e "If you are comfortable, you can gently close your eyes or look at the scene."
        e "Notice what you can see. Look at the colours, the light, and the waves."
        e "Now listen to the sounds."
        e "You may hear the waves, birds, or a gentle breeze."
        e "Now notice how your body feels."
        e "You may imagine warm sunlight, cool air, or soft sand under your feet."
        show hana smiling at hana_left
        e "Take a slow breath in."
        e "Now slowly breathe out."
        e "Stay in this peaceful place for a few moments."
        e "When you feel stressed, you can remember this calm beach and take a short pause."
        hide beachscene
        if music_pref:
            play music "audio/BGM/Hana_lofi.mp3" volume 0.2 fadein 3.0 loop

    return

#phase 5: closure 
label phase5_close_update(end_action):

    $ final_calm_text = "unknown"
    if last_calm_rating is not None:
        if last_calm_rating >= 4:
            $ final_calm_text = "calmer"
        elif last_calm_rating <= 2:
            $ final_calm_text = "still_stressed"
        else:
            $ final_calm_text = "in_between"

    python:
        assert session_id is not None and session_id != "", "ERROR: session_id must be set"
        assert user_name is not None and user_name.strip() != "", "ERROR: user_name must be set"
        assert session_filename is not None and session_filename.strip() != "", "ERROR: session_filename must be set"

        session_end_time = datetime.datetime.now()
        session_duration = (session_end_time - session_start_time).total_seconds() / 60.0
        calm_residual_factor = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.35, 5: 0.15}
        # End stress comes from this session's measured stress (the screening),
        # not the carried-over start, so a returning user's stress can end
        # higher OR lower than where their previous session left off.
        end_baseline = initial_stress_score if initial_stress_score else session_start_stress
        if calm_rated_this_session and last_calm_rating is not None:
            residual = calm_residual_factor.get(last_calm_rating, 1.0)
            session_end_stress = int(round(end_baseline * residual))
        else:
            # No calming rating was given this session, so this session's
            # measured (screening) stress stands as the end state. A stale
            # rating carried in from a previous visit must not be applied.
            session_end_stress = end_baseline

        stress_improvement = session_start_stress - session_end_stress

        profile = save_user_profile(user_name, {
            "name": user_name,
            "visit_count": user_profile.get("visit_count", 0) + 1,
            "last_session_id": session_id,
            "last_stress_score": session_end_stress,
            "last_stress_level": stress_level,
            "last_empathy_mode": last_empathy_mode,
            "last_intention_level": last_intention_level,
            "last_empathy_E": round(last_empathy_E, 4),
            "last_calm_rating": last_calm_rating,
            "last_technique": last_technique,
            "last_end_action": end_action,
            "support_need_announced": support_need_announced,
        })

        save_profile_slot(hana_selected_profile_slot, {
            "name": profile.get("name", user_name),
            "visit_count": profile.get("visit_count", 0),
            "last_session_id": profile.get("last_session_id", session_id),
            "last_stress_level": profile.get("last_stress_level", stress_level),
            "last_calm_rating": profile.get("last_calm_rating", last_calm_rating),
        })

        log_session_summary(
            session_filename, session_id, user_name,
            session_start_stress, session_end_stress,
            modes_used_list, techniques_used_list,
            interaction_count, last_calm_rating,
            round(session_duration, 2), end_action,
            stress_improvement,
            stress_level, last_empathy_mode, last_intention_level,
            round(last_empathy_E, 4), support_need_announced
        )

    # terus save after every flow nak avoid user tak save progress
    $ renpy.save("auto-1")

    show hana encouraging at hana_pos
    e "Thank you for spending this time with me, [user_name]."

    if final_calm_text == "calmer":
        $ close_line = renpy.random.choice([
            "I'm glad you're feeling a little calmer.",
            "Even feeling a little calmer is a good step.",
            "You took some time for yourself today, and that is important."
        ])
        e "[close_line!t]"
        show hana smiling at hana_pos
        e "Take care of yourself today."

    elif final_calm_text == "still_stressed":
        $ close_line = renpy.random.choice([
            "Even if you're still feeling stressed, you took time to check in with yourself today.",
            "You may not be feeling better yet, and that's okay.",
            "Sometimes it takes time to feel better, and that's okay."
        ])
        e "[close_line!t]"
        show hana concerned low at hana_pos
        e "If you're still finding things difficult, don't hesitate to talk to someone you trust."
        e "You do not have to go through this alone."
        show hana smiling at hana_pos
        e "I'll be here when you come back."

    else:
        $ close_line = renpy.random.choice([
            "We can keep taking things one step at a time.",
            "You do not have to feel completely okay for today to matter.",
            "Thank you for taking time to check in today."
        ])
        e "[close_line!t]"
        show hana smiling at hana_pos
        e "See you next time, [user_name]."
    stop music fadeout 5.0

    return



