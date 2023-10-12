#version 330

in vec3 position;
in vec3 color;

out vec3 newColor;
void main()
{
    gl_Position = vec4(position, 1.0f);
    newColor = color;
}