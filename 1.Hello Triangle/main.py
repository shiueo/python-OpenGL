import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy


def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)

    window = glfw.create_window(1200, 800, "1.Hello Triangle", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.3,
                0.5, -0.5, 0.0, 0.9, 0.5, 0.9,
                0.0, 0.5, 0.0, 0.2, 1.0, 1.0]

    triangle = numpy.array(triangle, dtype=numpy.float32)

    with open("./shaders/triangle.vert") as f:
        vertex_shader = f.read()

    with open("./shaders/triangle.frag") as f:
        fragment_shader = f.read()

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    glUseProgram(shader)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
