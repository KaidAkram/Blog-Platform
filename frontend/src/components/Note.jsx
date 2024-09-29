import React from "react";

function Note({note , onDelete}){ 
    const formattedDate = new Date(note.created_at).toLocaleString("en-US")

    return (
        <div className="note">
            <h1>{note.title}</h1>
            <p>{note.content}</p>
            <p>{formattedDate}</p>
            <button onClick={() => onDelete(note.id)}>DELETE</button>
        </div>
    )}