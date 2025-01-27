# Python Based Custom Interpreter

This project is a custom interpreter for a simple scripting language that integrates with Pygame. It allows you to create and manipulate game elements using a custom syntax.

## Features

- Basic Pygame integration
- Custom scripting language
- Sprite management
- Event handling
- Screen drawing and updating
- Print function for debugging

## How to Use

1. **Run the Interpreter**

   To run the interpreter, use the following command:
   ```sh
   python interpt.py <filename>.acd
   ```
   The file extension must be `.acd`.

2. **Script Syntax**

   - **Initialize Game**
     ```plaintext
     Game init <width> <height> <title>
     ```
     Example:
     ```plaintext
     Game init 600 400 Test
     ```

   - **Add Sprite**
     ```plaintext
     Game sprite add <x> <y> <color>
     ```
     Example:
     ```plaintext
     Game sprite add 0 0 blue
     ```

   - **Main Loop**
     ```plaintext
     while Game is running
         Game fill <r> <g> <b>
         Game events
         Game draw
         Game update
     end
     ```
     Example:
     ```plaintext
     while Game is running
         Game fill 255 0 0
         Game events
         Game draw
         Game update
     end
     ```

3. **Commands**

   - **Game Initialization**
     ```plaintext
     Game init <width> <height> <title>
     ```
     Initializes the game window with the specified width, height, and title.

   - **Add Sprite**
     ```plaintext
     Game sprite add <x> <y> <color>
     ```
     Adds a sprite at the specified coordinates with the given color.

   - **Fill Screen**
     ```plaintext
     Game fill <r> <g> <b>
     ```
     Fills the screen with the specified RGB color.

   - **Handle Events**
     ```plaintext
     Game events
     ```
     Processes Pygame events.

   - **Draw Sprites**
     ```plaintext
     Game draw
     ```
     Draws all sprites on the screen.

   - **Update Screen**
     ```plaintext
     Game update
     ```
     Updates the display.

   - **Check Game Running State**
     ```plaintext
     Game is running
     ```
     Checks if the game is still running.

## Example Script

```plaintext
import Game

Game init 600 400 Test

Game sprite add 0 0 blue

while Game is running
    Game fill 255 0 0
    Game events
    Game draw
    Game update
end
```

## Additional Information

- The interpreter is implemented in `interpt.py`.
- Pygame integration and sprite management are handled in `pygame_addon.py` and `pygame_addon_sprites.py`.

## References

- Inspired by the tutorial by [ComputerPhile](https://www.youtube.com/watch?v=Q2UDHY5as90&t=795s&ab_channel=Computerphile).