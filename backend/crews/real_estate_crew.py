from backend.tools.property_tools import PropertySearchTool

from crewai import (
    Crew,
    Task,
    Process
)

from backend.agents.lead_agent import (lead_agent)

from backend.agents.property_agent import (property_agent)

from backend.agents.market_agent import (market_agent)

from backend.agents.followup_agent import (followup_agent)

from backend.services.langfuse_service import (langfuse)



class RealEstateCrew:

    def run(
        self,
        customer_name,
        budget,
        property_type,
        timeline,
        location
    ):

        
        lead_task = Task(
            description=f"""
            Analyze the lead.

            Customer Name:
            {customer_name}

            Budget:
            PKR {budget:,}

            Property Type:
            {property_type}

            Timeline:
            {timeline}

            Determine:

            1. Lead score (0-100)
            2. Priority
            3. Reasoning
            """,

            expected_output="""
            Lead score,
            priority,
            and explanation.
            """,

            agent=lead_agent
        )
        
        property_tool = PropertySearchTool()
        matching_properties = property_tool._run(
            budget=budget,
            property_type=property_type,
            location=location
        )
        
        property_task = Task(
           description=f"""
            Customer requirements:

            Budget: PKR {budget:,}
            Property Type: {property_type}
            Location: {location}

            Available matching properties:
            {matching_properties}

            Create a professional recommendation report.

            Use ONLY the properties listed above.
            Do not invent additional properties.
            """,
            expected_output="""
            Property recommendations.
            """,
            context=[lead_task],
            agent=property_agent
        )

        
        market_task = Task(
            description=f"""
            Analyze the neighborhood around:

            Location:
            {location}

            You MUST use the Neighborhood Intelligence Tool
            to retrieve real neighborhood data.

            Do not make assumptions.
            Do not invent schools, hospitals, parks,
            shopping malls or metro stations.

            Use only the information returned
            by the tool.

            Produce a report containing:

            1. Nearby Schools
            2. Nearby Hospitals
            3. Nearby Parks
            4. Nearby Shopping Malls
            5. Nearby Metro Stations

            Summarize why the location
            may be attractive for buyers.
            """,

            expected_output="""
            A professional neighborhood
            intelligence report.
            """,

            context=[
                lead_task,
                property_task
            ],

            agent=market_agent
        )

        
        followup_task = Task(
            description=f"""
            Create a professional follow-up email.

            Customer:
            {customer_name}

            Property Type:
            {property_type}

            Location:
            {location}

            Write a concise and professional email.
            """,

            expected_output="""
            Email subject and body.
            """,

            context=[lead_task, property_task, market_task],

            agent=followup_agent
        )

        
        crew = Crew(
            agents=[
                lead_agent,
                property_agent,
                market_agent,
                followup_agent
            ],

            tasks=[
                lead_task,
                property_task,
                market_task,
                followup_task
            ],

            process=Process.sequential,

            verbose=True
        )

        with langfuse.start_as_current_observation(
            as_type="span",
            name="real-estate-analysis"
        ):
    
            crew_output = crew.kickoff()

        langfuse.flush()

        
        return {
            "lead_analysis": crew_output.tasks_output[0].raw, 
            
            "property_recommendations": crew_output.tasks_output[1].raw, 
            
            "neighborhood_intelligence": crew_output.tasks_output[2].raw, 
            
            "followup_email": crew_output.tasks_output[3].raw
            }             
        
