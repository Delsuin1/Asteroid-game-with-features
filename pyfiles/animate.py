import pygame
# position default = 0
def animate(sprite_sheet, num_col, num_rows, radius, start_row, start_col, rotation=0):
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // num_col
        frame_height = sheet_height // num_rows
        
        frames_list = []


        for row in range(start_row):
            for col in range(start_col):
                rect = pygame.Rect(
                    col * frame_width,
                    row * frame_height, 
                    frame_width, 
                    frame_height
                )
                frame = sprite_sheet.subsurface(rect)
                resized_frame = pygame.transform.rotozoom(frame,rotation,radius)
                
                frames_list.append(resized_frame)
        return frames_list, resized_frame