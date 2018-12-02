#!/usr/bin/env python3

import chess
import cherrypy

if __name__ == '__main__':
	board = chess.Board()
	new_moves = board.legal_moves()
	


# vim: tabstop=4 shiftwidth=4 noexpandtab
