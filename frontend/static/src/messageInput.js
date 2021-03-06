import React, { useRef } from 'react';

function MessageInput() {
    const messageInput = useRef(null);
    messageInput.current.focus();

    return (
        <div>
            <textarea id="chat-message-input" type="text" cols="100" />
            <br />
            <input id="chat-message-submit" type="button" className="button" value="Send" />
        </div>
    );
}

export default MessageInput;