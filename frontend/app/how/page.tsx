"use client"

import { useRouter } from "next/navigation"

export default function HowItWorks() {

  const router = useRouter()

  return (

    <div style={{padding:20,fontFamily:"Arial"}}>

      <h1>How NewsAgentAI Works</h1>

      <p style={{marginTop:10}}>
        NewsAgentAI is a lightweight learning AI agent that continuously monitors
        RSS news feeds and detects emerging topics.
      </p>

      <p>
        The backend agent fetches articles, extracts topics, and scores them
        using several signals such as frequency, growth, spread, and persistence.
      </p>

      <p>
        A monitoring loop updates topic scores over time. Rapid acceleration
        in topic activity is detected as a "spike", while slower consistent
        growth appears as a "trend".
      </p>

      <p>
        The agent also adjusts internal weights over time based on observed
        topic behavior, allowing the system to gradually improve how it
        detects meaningful patterns in news activity.
      </p>

      <p>
        The dashboard polls the backend periodically to display the latest
        detected spikes, trends, and the current learned weights.
      </p>


      <button
        onClick={()=>router.push("/")}
        style={{
          marginTop:20,
          padding:"10px 16px",
          background:"#0070f3",
          color:"white",
          border:"none",
          borderRadius:6,
          cursor:"pointer"
        }}
      >
        ← Back to Dashboard
      </button>

    </div>

  )

}