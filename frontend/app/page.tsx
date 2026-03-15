"use client"

import { useEffect, useState } from "react"
import Link from "next/link"

export default function Dashboard() {

  const [tick, setTick] = useState(0)
  const [trends, setTrends] = useState<any[]>([])
  const [spikes, setSpikes] = useState<any[]>([])
  const [weights, setWeights] = useState<any>({})
  const [timestamp, setTimestamp] = useState("")

  // polling timer
  useEffect(() => {

    const id = setInterval(() => {
      setTick(t => t + 1)
    }, 5000)

    return () => clearInterval(id)

  }, [])


  // fetch server data
  useEffect(() => {

    async function fetchData() {

      try {

        const res = await fetch("http://localhost:8000/trends")
        const data = await res.json()

        setTrends(data.trends || [])
        setSpikes(data.spikes || [])
        setWeights(data.weights || {})
        setTimestamp(data.timestamp || "")

      } catch (err) {

        console.log("fetch error", err)

      }

    }

    fetchData()

  }, [tick])


  return (

    <div style={{padding:20,fontFamily:"Arial"}}>

      <h1>NewsAgentAI Dashboard</h1>

      <Link href="/how">How It Works</Link>

      <p style={{marginTop:10,color:"#777"}}>
        Last update: {timestamp}
      </p>


      <div style={{
        display:"flex",
        gap:20,
        marginTop:20
      }}>


        {/* SPIKES PANEL */}

        <div style={{
          flex:1,
          background:"#111",
          color:"white",
          padding:15,
          borderRadius:10
        }}>

          <h2>⚡ Spikes</h2>

          {spikes.map((s:any,i:number)=>(
            <div key={i} style={{
              background:"#1f1f1f",
              padding:8,
              marginBottom:6,
              borderRadius:6
            }}>
              {s.topic} ({s.score})
            </div>
          ))}

        </div>


        {/* TRENDS PANEL */}

        <div style={{
          flex:1,
          background:"#111",
          color:"white",
          padding:15,
          borderRadius:10
        }}>

          <h2>📈 Trends</h2>

          {trends.map((t:any,i:number)=>(
            <div key={i} style={{
              background:"#1f1f1f",
              padding:8,
              marginBottom:6,
              borderRadius:6
            }}>
              {t.topic} ({t.score})
            </div>
          ))}


          {/* WEIGHTS */}

          <div style={{
            marginTop:20,
            background:"#222",
            padding:10,
            borderRadius:8
          }}>

            <h3>Learned Weights</h3>

            <div>frequency: {weights.frequency}</div>
            <div>growth: {weights.growth}</div>
            <div>spread: {weights.spread}</div>
            <div>persistence: {weights.persistence}</div>

          </div>

        </div>

      </div>

    </div>

  )

}