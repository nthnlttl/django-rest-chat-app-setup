import React from 'react';

function Message(props) {
    const { text, date } = props;
    return (
        <div id="message" className="card">
            <div className="cell large-4">
                {text}
            </div>
            <div className="cell large-2 text-right"><small>{date}</small></div>
        </div>
    );
}

export default Message;