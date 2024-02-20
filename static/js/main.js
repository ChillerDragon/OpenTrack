const backendUrl = '/api/v1'

window.addEventListener('mousemove', (event) => {
  console.log(event)
  const mouseMove = {
    pageX: event.pageX,
    pageY: event.pageY,
    screenX: event.screenX,
    screenY: event.screenY
  }
  fetch(`${backendUrl}/mouse_move`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(mouseMove)
  })
})
