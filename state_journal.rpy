# state_journal.rpy
# Journal structures: Today, People, Dreams, Player Notes (foundation).

init -20 python:
    class JournalState(object):
        def __init__(self):
            # day_number -> {"summary": str, "events": [str]}
            self.day_log = {}
            # npc_id -> {"bio": str, "likes": [], "dislikes": [], "memories": []}
            self.people = {}
            # dream entity id -> {"name": str, "domain": str, "notes": [str], "status": "seen|fought|integrated|avoided"}
            self.dreams = {}
            # free-form player notes
            self.player_notes = []  # list of {"day": d, "segment": s, "tag": t, "text": txt}

        def _ensure_day(self, day):
            if day not in self.day_log:
                self.day_log[day] = {"summary": "", "events": []}

    # --- Top-level helpers (use the global 'journal' instance) ---

    def journal_add_today_event(text, arete_hint=None):
        day = gs.day_number
        journal._ensure_day(day)
        if arete_hint:
            event_line = u"%s  [%s]" % (text, arete_hint)
        else:
            event_line = text
        journal.day_log[day]["events"].append(event_line)

    def journal_set_summary(day, text):
        journal._ensure_day(day)
        journal.day_log[day]["summary"] = text

    def journal_add_memory(npc_id, text):
        p = journal.people.setdefault(npc_id, {"bio":"", "likes":[], "dislikes":[], "memories":[]})
        p["memories"].append(text)

    def journal_update_npc_stage(npc_id):
        # convenience (stage computed from gs.npcs) — no-op for now
        pass

    def journal_note_dream(entity_id, name, domain, note, status="seen"):
        entry = journal.dreams.setdefault(entity_id, {"name": name, "domain": domain, "notes": [], "status": status})
        entry["status"] = status
        entry["notes"].append(note)

    def journal_add_player_note(tag, text):
        journal.player_notes.append({
            "day": gs.day_number,
            "segment": gs.time_segment,
            "tag": tag,
            "text": text
        })

# Global instances / selection state
default journal = JournalState()
default journal_selected_friend = None
default journal_selected_dream = None
