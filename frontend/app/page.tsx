"use client"

import { useEffect, useState } from "react"
import Link from "next/link"

export default function Home() {

  const [data,setData] = useState({trends:[],spikes:[]})

  async function load(){

    const res = await fetch("http://127.0.0.1:8000/trends")
    const json = await res.json()

    setData(json)

  }

  useEffect(()=>{

    load()

    const timer = setInterval(load,10000)

    return ()=>clearInterval(timer)

  },[])

  return (

    <div style={{
      fontFamily:"Arial",
      background:"#f5f6fa",
      minHeight:"100vh"
    }}>

      {/* HEADER */}

      <div style={{
        background:"#1e293b",
        color:"white",
        padding:20,
        textAlign:"center"
      }}>
        <h1>AI News Trend Agent</h1>

        <Link href="/how">
          <button style={{
            marginTop:10,
            padding:"8px 16px",
            cursor:"pointer"
          }}>
            How it Works?
          </button>
        </Link>
      </div>


      {/* DASHBOARD */}

      <div style={{
        maxWidth:1000,
        margin:"40px auto",
        display:"grid",
        gridTemplateColumns:"1fr 1fr",
        gap:30
      }}>

        {/* SPIKES */}

        <div style={{
          background:"white",
          padding:25,
          borderRadius:10,
          boxShadow:"0 2px 10px rgba(0,0,0,0.1)"
        }}>

          <h2 style={{color:"#e11d48"}}>Spike Alerts</h2>

          <ul>
          {data.spikes.length === 0 && (
            <div style={{padding:30}}>Agent collecting Spike signals...</div>
      )}
          {data.spikes.map((s:any)=>(
            <li key={s.topic} style={{marginBottom:10}}>
              {s.topic}
              <br/>
              <small>spike score: {s.spike_score}</small>
            </li>
          ))}

          </ul>

        </div>


        {/* TRENDS */}

        <div style={{
          background:"white",
          padding:25,
          borderRadius:10,
          boxShadow:"0 2px 10px rgba(0,0,0,0.1)"
        }}>

          <h2 style={{color:"#2563eb"}}>Top Trends</h2>

          <ul>
          {data.trends.length === 0 && (
            <div style={{padding:30}}>Agent collecting Trend signals...</div>
          )}
          {data.trends.map((t:any)=>(
            <li key={t.topic} style={{marginBottom:10}}>
              {t.topic}
              <br/>
              <small>trend score: {t.trend_score}</small>
            </li>
          ))}

          </ul>

        </div>

      </div>

    </div>

  )
}
