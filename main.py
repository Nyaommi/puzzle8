import pygame
import random

pygame.init()

width = 900
height = 900
squareSize = width//3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3x3 Puzzle")

def createBoard():
  numbers = list(range(1,9)) + [0]
  random.shuffle(numbers)
  return [numbers[i:i+3] for i in range(0,9,3)]

def drawBoard(board):
  screen.fill((255,255,255))
  font = pygame.font.Font(None, 100)

  for row in range(3):
    for col in range(3):
      number = board[row][col]
      if number != 0:
        square = pygame.Rect(col*squareSize, row*squareSize, squareSize, squareSize)
        pygame.draw.rect(screen, (0,0,0), square, 5)
        text = font.render(str(number), True, (0,0,0))
        screen.blit(text, text.get_rect(center=square.center))

def findSpace(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == 0:
        return row, col
    
def movePiece(board, direction):
  emptyRow, emptyCol = findSpace(board)
  if direction == 'arriba' and emptyRow < 2:
    board[emptyRow][emptyCol], board[emptyRow+1][emptyCol] = board[emptyRow+1][emptyCol], board[emptyRow][emptyCol]
  elif direction == 'abajo' and emptyRow > 0:
    board[emptyRow][emptyCol], board[emptyRow-1][emptyCol] = board[emptyRow-1][emptyCol], board[emptyRow][emptyCol]
  elif direction == 'izquierda' and emptyCol < 2:
    board[emptyRow][emptyCol], board[emptyRow][emptyCol+1] = board[emptyRow][emptyCol+1], board[emptyRow][emptyCol]
  elif direction == 'derecha' and emptyCol > 0:
    board[emptyRow][emptyCol], board[emptyRow][emptyCol-1] = board[emptyRow][emptyCol-1], board[emptyRow][emptyCol]

def winCondition(board):
  return board == [[1,2,3],[4,5,6,],[7,8,0]]

def main():
  board = createBoard()
  clock = pygame.time.Clock()
  gameLoop = True

  while gameLoop:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameLoop = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          movePiece(board, 'arriba')
        elif event.key == pygame.K_DOWN:
          movePiece(board, 'abajo')
        elif event.key == pygame.K_LEFT:
          movePiece(board, 'izquierda')
        elif event.key == pygame.K_RIGHT:
          movePiece(board, 'derecha')
    drawBoard(board)

    if winCondition(board):
      font = pygame.font.Font(None, 50)
      text = font.render("You Win!", True, (0,128,0))
      screen.blit(text, text.get_rect(center = screen.get_rect().center))
      pygame.display.flip()
      pygame.time.wait(2000)
      gameLoop = False

    pygame.display.flip()
    clock.tick(30)
  pygame.quit()

if __name__ == '__main__':
  main()