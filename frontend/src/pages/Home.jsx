import react from 'react'
import { useState , useEffect } from 'react'
import Note from '../components/Note'

function Home ()  {
  const [notes, setNotes] = useState([])
  const [content , setContent] = useState('')
  const [title , setTitle] = useState('')
  useEffect(() => {
    getNotes();
  })

  const getNotes = async () =>{
    api.get("/api/notes/").then((res) => res.data).then((data) => setNotes(data)).catch((err) => console.log(err))
  }

  const deleteNote = async (id) =>{
    api.delete(`/api/notes/${id}/`).then((res) => res.data).then((data) => getNotes()).catch((err) => console.log(err))
  }

  const createNote = async (e) =>{
    e.preventDefault()
    api.post("/api/notes/", {title , content}).then((res) => res.data).then((data) => getNotes()).catch((err) => console.log(err))
  }
  return (
    <div>
      <h1>notes</h1>
      {notes.map((note) => (
        <Note note = {note} onDelete = {deleteNote}  key={note.id}/>
      ))}
      <h2>
        create note
      </h2>
      <form onSubmit={createNote}>
        <input type="text" placeholder='title'  value={title} onChange={(e) => setTitle(e.target.value)} />
        <input type="text" placeholder='content'  value={content} onChange={(e) => setContent(e.target.value)} />
        <input type="submit" value="create note" />
      </form>
      </div>
  )
}

export default Home
