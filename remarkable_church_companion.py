import io
import textwrap
from datetime import datetime

import streamlit as st
from docx import Document  # pip install python-docx


# ---------- CONFIG ----------
st.set_page_config(
    page_title="Remarkable Church Companion (RCC.AI)",
    page_icon="⛪",
    layout="wide",
)

# ---------- HELPERS ----------

def wrap(text):
    return textwrap.fill(text, width=100)


def estimate_demographics(zip_code: str):
    """
    Very simple helper.
    You can customize this later with real census data if you want.
    For now, we assume Tulsa ZIP codes start with '741'.
    """
    if zip_code.strip().startswith("741"):
        return {
            "city_name": "Tulsa",
            "summary": (
                "Tulsa is a mid-sized city with many working-age adults, "
                "young families, and significant economic diversity."
            ),
            "ministry_implications": (
                "A strong focus on next-gen (youth and young adults), small groups, "
                "family discipleship, and compassionate outreach to those in need."
            ),
        }
    else:
        return {
            "city_name": "your community",
            "summary": (
                "This area likely includes a mix of families, workers, and students "
                "with varied spiritual backgrounds."
            ),
            "ministry_implications": (
                "Build bridges through relationships, small groups, youth ministry, "
                "and consistent community presence."
            ),
        }


def generate_12_month_plan(
    church_name,
    mission,
    avg_attendance,
    youth_count,
    volunteer_capacity,
    budget_level,
    demographics,
):
    """
    Returns a big string describing a quarter-by-quarter plan using
    the Remarkable Church / Project 13 style frameworks.
    """

    # Simple scaling text based on inputs
    size_label = "smaller" if avg_attendance <= 150 else "medium-sized or larger"
    youth_label = "modest" if youth_count <= 20 else "strong"
    budget_text = {
        "Low": "a lean, highly relational approach with creative, low-cost strategies.",
        "Medium": "balanced use of relational and program-based strategies with moderate event investment.",
        "High": "larger events, more frequent gatherings, and robust resource investment for teams and tech.",
    }[budget_level]

    dem_city = demographics["city_name"]
    dem_summary = demographics["summary"]
    dem_implications = demographics["ministry_implications"]

    text = f"""
12-MONTH IMPLEMENTATION PLAN FOR {church_name.upper()}

Mission / DNA:
{wrap(mission)}

Local Context:
- Community: {dem_city}
- Snapshot: {wrap(dem_summary)}
- Ministry implications: {wrap(dem_implications)}

Church Profile:
- Average weekly attendance: ~{avg_attendance} ({size_label} congregation)
- Estimated youth / next-gen: ~{youth_count} ({youth_label} base to build on)
- Volunteer capacity: ~{volunteer_capacity} active volunteers
- Budget level for next-gen & outreach: {budget_level} – this suggests {budget_text}

YEARLY BIG-PICTURE GOALS (End of 12 Months):
- Strengthen a clear next-gen discipleship pipeline (ages 13–21).
- Grow a culture of warm relationships, mentoring, and “sticky” community.
- Host at least one Epic Event as a catalytic moment for outreach.
- Increase engagement in small groups and serving.
- Build a youth leadership pipeline including mentoring and ministry roles.

--------------------------------------------------
QUARTER 1 (Months 1–3): FOUNDATION & ASSESSMENT
--------------------------------------------------
Focus: Clarify who we are, who we are reaching, and what health looks like.

Month 1 – Listen & Clarify:
- Conduct a simple church-wide survey (paper or digital) to learn:
  - Spiritual growth needs
  - Interest in small groups
  - Skills and availability for serving
- Re-articulate the mission and vision from the platform and in small meetings.
- Preach/teach on God’s heart for the next generation (Psalm 78, Mark 3, etc.).

Month 2 – Pilot Community Structures:
- Launch 1–2 pilot small groups (e.g., young adults, young families, mixed group).
- Identify 5–8 “implementation champions” (potential leaders) to form a core team.
- Begin informal youth hangouts (e.g., after church, simple mid-week connection).

Month 3 – Map the Community & Build Systems:
- Identify key neighborhoods and schools around the church in {dem_city}.
- Start a simple “Next-Gen Dashboard”:
  - Youth present, visitors, follow-ups, new small group members.
- Hold a “Vision Night” for youth and parents to share the year plan.

--------------------------------------------------
QUARTER 2 (Months 4–6): SYSTEMS & DISCIPLESHIP PATHWAYS
--------------------------------------------------
Focus: Build clear pathways using Precision Discipleship and 72-Hour Follow-Up concepts.

Month 4 – Precision Discipleship Pathway:
- Define what a mature 21-year-old disciple looks like in your context:
  - Scripture engagement, prayer, community, serving, evangelism.
- Create simple milestones for ages 13–21 (e.g., first serving role, first Bible reading plan, first mission/outreach).
- Communicate this pathway visually (poster, handout, slide).

Month 5 – Small Groups & Mentoring:
- Expand to 3–4 small groups, ensuring at least one group focuses on next-gen-or-young adults.
- Pair each youth with a caring adult or older peer as a mentor.
- Train mentors with 3–4 simple questions:
  - “How are you really?”
  - “Where did you see God this week?”
  - “What is one step of obedience you sense God inviting you to take?”
  - “How can I pray for you?”

Month 6 – Follow-Up & Engagement:
- Implement a 72-Hour Follow-Up for all new youth/visitors:
  - Within 24 hours: warm text or call.
  - Within 72 hours: invite to small group or next gathering.
- Begin planning the Epic Event for Quarter 3:
  - Define purpose: outreach, recommitment, on-ramp into groups.
  - Set prayer emphasis for the event.

--------------------------------------------------
QUARTER 3 (Months 7–9): EPIC EVENT & MOMENTUM
--------------------------------------------------
Focus: Host a catalytic Epic Event and turn decisions into discipleship.

Month 7 – Pre-Event Incubation:
- Ask every small group to pray for and list 3–5 people to invite.
- Strengthen relational bridges:
  - Host one pre-event social (game night, BBQ, park hangout).
- Finalize Epic Event details (date, theme, speakers, worship, teams).

Month 8 – Epic Event:
- Execute the event with excellence and warmth:
  - Clear welcome, clear gospel presentation, clear next steps.
- Capture contact info for all guests (cards, QR code, or text sign-up).
- Same-day micro-follow-up:
  - Hand them next-steps info (small groups, youth nights, mentoring).

Month 9 – Post-Event Integration:
- Use the 72-Hour Follow-Up plan to contact every guest.
- Launch short-term “On-Ramp Groups” or classes for new people:
  - 4–6 weeks focused on basics: Who is Jesus? What is church? Why community?
- Invite engaged youth into a 12-week Youth Leadership Track:
  - Character, Scripture, prayer, serving, basic evangelism.

--------------------------------------------------
QUARTER 4 (Months 10–12): CONSOLIDATION & MULTIPLICATION
--------------------------------------------------
Focus: Solidify rhythms, multiply leaders, and prepare for the next year.

Month 10 – Evaluate & Celebrate:
- Gather leaders to review:
  - Attendance trends (Sundays, youth, small groups).
  - Stories of life change (testimonies, answered prayers).
  - Volunteer health and needs.
- Share stories from the platform to build faith and buy-in.

Month 11 – Leadership Pipeline:
- Continue or repeat the Youth Leadership Track for new students.
- Identify potential new small-group leaders and co-leaders.
- Offer training on:
  - Leading discussions
  - Caring for people
  - Empowering others to serve

Month 12 – Plan the Next 12 Months:
- Revisit mission, vision, and key metrics.
- Decide:
  - How many Epic Events next year?
  - Which small groups will continue or multiply?
  - What new outreach expressions to start (e.g., school partnerships, service projects)?
- Commission leaders publicly and pray for the next year’s harvest.

This plan is a flexible template. You can adjust details, but the flow remains:
FOUNDATION → PATHWAYS → EPIC CATALYST → CONSOLIDATION & MULTIPLICATION.
"""
    return text


def calculate_epic_event_cost(event_size: int, budget_level: str):
    """
    Very simple cost model you can tweak.
    """
    base_per_person = {
        "Low": 8,     # snacks, simple print materials, minimal extras
        "Medium": 15, # more robust food, basic production, decor
        "High": 25,   # higher-end experience, strong production, merch, etc.
    }[budget_level]

    total_cost = base_per_person * event_size
    marketing = total_cost * 0.25
    food_beverage = total_cost * 0.4
    production = total_cost * 0.25
    contingency = total_cost * 0.1

    return {
        "total_cost": round(total_cost),
        "marketing": round(marketing),
        "food_beverage": round(food_beverage),
        "production": round(production),
        "contingency": round(contingency),
    }


def generate_measurables(avg_attendance, youth_count, volunteer_capacity, event_size):
    """
    Generates simple, scaled numeric targets.
    """
    target_attendance = int(avg_attendance * 1.5)
    target_small_groups = max(3, avg_attendance // 40)
    target_youth_leaders = max(4, youth_count // 3)
    target_volunteers = max(volunteer_capacity + 10, int(avg_attendance * 0.4))
    target_guests = int(event_size * 0.5)
    target_decisions = max(5, event_size // 10)

    return {
        "attendance_goal": target_attendance,
        "small_groups_goal": target_small_groups,
        "youth_leaders_goal": target_youth_leaders,
        "volunteers_goal": target_volunteers,
        "epic_event_guests_goal": target_guests,
        "decisions_goal": target_decisions,
    }


def create_docx_from_plan(plan_text: str, church_name: str) -> bytes:
    """
    Creates a .docx file in memory from the plan text and returns raw bytes.
    """
    doc = Document()
    doc.add_heading(f"12-Month Implementation Plan – {church_name}", level=1)

    # Split on double newlines to create paragraphs/sections
    for block in plan_text.strip().split("\n\n"):
        doc.add_paragraph(block)

    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()


# ---------- UI ----------

st.title("⛪ Remarkable Church Companion (RCC.AI)")
st.caption(
    "An implementation helper for Remarkable Church principles & Project 13 "
    "— built for pastors and church leaders."
)

st.markdown("---")

with st.sidebar:
    st.subheader("Church Profile")
    church_name = st.text_input("Church name", value="Peniel Baptist Church")
    mission = st.text_area(
        "Church mission / vision",
        value="To glorify God by making disciples of Jesus among families, youth, and the community.",
        height=80,
    )
    avg_attendance = st.number_input(
        "Average weekly attendance",
        min_value=20,
        max_value=10000,
        value=120,
        step=5,
    )
    youth_count = st.number_input(
        "Estimated youth / next-gen (ages 13–25)",
        min_value=0,
        max_value=2000,
        value=25,
        step=1,
    )
    volunteer_capacity = st.number_input(
        "Active volunteers currently serving",
        min_value=5,
        max_value=2000,
        value=25,
        step=1,
    )
    budget_level = st.selectbox(
        "Budget level for next-gen & outreach",
        options=["Low", "Medium", "High"],
        index=1,
    )
    zip_code = st.text_input("Church ZIP code", value="74104")

    st.markdown("---")
    st.subheader("Epic Event Planner")
    event_size = st.number_input(
        "Desired Epic Event size (people)",
        min_value=50,
        max_value=5000,
        value=300,
        step=25,
    )

    generate_button = st.button("🚀 Generate Plan")

# Main content columns
col_plan, col_metrics = st.columns([2, 1])

if generate_button:
    demographics = estimate_demographics(zip_code)
    plan_text = generate_12_month_plan(
        church_name=church_name,
        mission=mission,
        avg_attendance=avg_attendance,
        youth_count=youth_count,
        volunteer_capacity=volunteer_capacity,
        budget_level=budget_level,
        demographics=demographics,
    )
    cost = calculate_epic_event_cost(event_size, budget_level)
    measurables = generate_measurables(
        avg_attendance, youth_count, volunteer_capacity, event_size
    )

    with col_plan:
        st.subheader("📆 12-Month Implementation Plan")
        st.markdown(f"**Generated for:** {church_name}")
        st.markdown(f"_As of {datetime.now().strftime('%B %d, %Y')}._")

        st.code(plan_text, language="markdown")

        # ---- DOWNLOAD BUTTONS ----
        st.markdown("### ⬇️ Download This Plan")

        # TXT download
        st.download_button(
            label="Download as .txt",
            data=plan_text,
            file_name=f"{church_name.replace(' ', '_').lower()}_12_month_plan.txt",
            mime="text/plain",
        )

        # DOCX download
        docx_bytes = create_docx_from_plan(plan_text, church_name)
        st.download_button(
            label="Download as .docx (Word)",
            data=docx_bytes,
            file_name=f"{church_name.replace(' ', '_').lower()}_12_month_plan.docx",
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
        )

    with col_metrics:
        st.subheader("💰 Epic Event Cost Estimate")
        st.write(f"**Event size:** {event_size} people")
        st.write(f"**Budget level:** {budget_level}")
        st.metric("Estimated Total Cost", f"${cost['total_cost']:,}")
        st.write("Breakdown (approx.):")
        st.write(f"- Marketing & promotion: **${cost['marketing']:,}**")
        st.write(f"- Food & beverages: **${cost['food_beverage']:,}**")
        st.write(f"- Production & environment: **${cost['production']:,}**")
        st.write(f"- Contingency: **${cost['contingency']:,}**")

        st.markdown("---")
        st.subheader("📊 Measurable Goals")

        st.write("**Tangible Targets (by end of 12 months):**")
        st.write(f"- Average weekly attendance: **~{measurables['attendance_goal']}**")
        st.write(f"- Active small groups: **{measurables['small_groups_goal']}**")
        st.write(f"- Youth / young adult leaders: **{measurables['youth_leaders_goal']}**")
        st.write(f"- Active volunteers: **{measurables['volunteers_goal']}**")
        st.write(
            f"- Guests at Epic Event from outside church: **~{measurables['epic_event_guests_goal']}**"
        )
        st.write(f"- Decisions / commitments to Christ: **≥ {measurables['decisions_goal']}**")

        st.write("**Intangible Outcomes to Watch:**")
        st.write("• Increased sense of belonging among youth and newcomers.")
        st.write("• Stronger intergenerational relationships and mentoring.")
        st.write("• Greater ownership of ministry among volunteers and youth.")
        st.write("• Stories of answered prayer, restored families, and transformed lives.")

else:
    with col_plan:
        st.info(
            "Fill out the church profile on the left, set your desired Epic Event size, "
            "and click **“🚀 Generate Plan”** to create a customized 12-month plan."
        )
    with col_metrics:
        st.info(
            "Epic Event costs and measurable goals will appear here once you generate the plan."
        )
